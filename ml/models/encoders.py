import torch
import torch.nn as nn

class ModalityEncoder(nn.Module):
    """
    Encodes a single continuous modality sequence.
    Architecture: 1D-CNN (for local temporal feature extraction) -> BiLSTM (for temporal aggregation).
    """
    def __init__(self, in_channels: int, cnn_out_channels: int, cnn_kernel_size: int, bilstm_hidden_size: int, dropout_p: float = 0.15):
        super().__init__()
        
        # 1D-CNN expects shape [batch_size, channels, sequence_length]
        # We assume padding='same' to keep sequence length unchanged
        self.cnn = nn.Conv1d(
            in_channels=in_channels,
            out_channels=cnn_out_channels,
            kernel_size=cnn_kernel_size,
            padding=cnn_kernel_size // 2
        )
        self.relu = nn.ReLU()
        self.dropout1 = nn.Dropout(dropout_p)
        
        # BiLSTM expects shape [batch_size, sequence_length, input_size] when batch_first=True
        self.lstm = nn.LSTM(
            input_size=cnn_out_channels,
            hidden_size=bilstm_hidden_size,
            num_layers=1,
            batch_first=True,
            bidirectional=True
        )
        self.dropout2 = nn.Dropout(dropout_p)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        x: Tensor of shape [batch_size, seq_len, in_channels]
        Returns: Tensor of shape [batch_size, seq_len, 2 * bilstm_hidden_size]
        """
        # Convert to [batch_size, in_channels, seq_len] for 1D-CNN
        x = x.transpose(1, 2)
        
        x = self.cnn(x)
        x = self.relu(x)
        x = self.dropout1(x)
        
        # Convert back to [batch_size, seq_len, cnn_out_channels] for LSTM
        x = x.transpose(1, 2)
        
        # LSTM output shape: [batch_size, seq_len, 2 * bilstm_hidden_size]
        out, _ = self.lstm(x)
        out = self.dropout2(out)
        
        return out
