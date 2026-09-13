# LITERATURE → MESH IMPLEMENTATION MAP

The DA1 report reviewed 15 references. This document records how the reported evidence informs MESH without copying paper results into MESH.

## References 1–5

1. **HEDLF / industrial multimodal fusion** — architectural context for CNN/BiLSTM/attention and explainability.
2. **MDPI multimodal sensor fusion** — supports combining modalities; the report notes explicit dropped-channel handling was absent.
3. **Multi-sensor fusion review** — motivates comparison of concatenation, decision, and hybrid fusion.
4. **Multiscale transfer-learning RUL** — motivates multiscale temporal representation and possible transfer-learning experiments when justified.
5. **2025 turbofan RUL study** — broader RUL/prognostics context.

## References 6–15

6. **Missing-modality survey** — conceptual basis for modality masking/dropout.
7. **CNN-BiGRU + attention bearing diagnosis** — supports convolutional/recurrent temporal representation.
8. **Cross-space multiscale CNN-Transformer bearing diagnosis** — comparison context for multiscale/Transformer approaches.
9. **e-CNN-GRU-SAM** — attention/staged degradation context.
10. **Parallel 1D-CNN bearing diagnosis** — baseline/alternative temporal feature extraction.
11. **Parallel CNN + LSTM bearing diagnosis** — supports CNN + recurrent encoding.
12. **GPT-based RUL prediction** — literature context only; an LLM is not required for numerical time-series prediction.
13. **AI4I-PMDI** — highlights irregularities and missingness effects.
14. **Missing-modality medical fusion** — methodological analogue, not industrial evidence.
15. **AI4I XGBoost/sliding-window work** — classical benchmark context, not proof of real industrial generalization.

## What the literature does not justify

- copying reported SOTA metrics;
- claiming production reliability;
- treating AI4I as real industrial evidence;
- treating attention as causal explanation;
- adding an LLM just to make the product look advanced.

## What the literature supports testing

- CNN + recurrent encoders;
- attention fusion;
- missing-modality masks/dropout;
- temporal refinement;
- explainability;
- grouped evaluation;
- ablation studies.

## References from the DA1 report

[1] https://www.researchsquare.com/article/rs-10228081/v1

[2] https://www.mdpi.com/2075-1702/10/11/1105

[3] https://link.springer.com/article/10.1007/s00170-026-17965-2

[4] https://academic.oup.com/jcde/article/11/1/343/7610897

[5] https://www.nature.com/articles/s41598-025-09155-z

[6] https://arxiv.org/html/2409.07825v1

[7] https://link.springer.com/article/10.1007/s12206-024-0610-2

[8] https://www.nature.com/articles/s41598-025-95895-x

[9] https://www.nature.com/articles/s41598-025-17008-y

[10] https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0327206

[11] https://www.aimspress.com/article/doi/10.3934/mbe.2024105

[12] https://dl.acm.org/doi/fullHtml/10.1145/3674399.3674456

[13] https://www.sciencedirect.com/science/article/pii/S1877050924025912

[14] https://arxiv.org/abs/2309.15529

[15] https://thesai.org/Publications/ViewPaper?Volume=16&Issue=10&Code=IJACSA&SerialNo=27
