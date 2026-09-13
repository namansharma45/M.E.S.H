import os
import json
from datetime import datetime

class ExperimentTracker:
    def __init__(self, log_dir: str, experiment_name: str):
        self.run_dir = os.path.join(log_dir, experiment_name)
        os.makedirs(self.run_dir, exist_ok=True)
        self.log_file = os.path.join(self.run_dir, "metrics.jsonl")
        
    def log_metrics(self, metrics: dict, step: int, prefix: str = "train"):
        log_entry = {"step": step, "timestamp": datetime.now().isoformat()}
        for k, v in metrics.items():
            log_entry[f"{prefix}/{k}"] = v
            
        with open(self.log_file, "a") as f:
            f.write(json.dumps(log_entry) + "\n")
            
    def close(self):
        pass
