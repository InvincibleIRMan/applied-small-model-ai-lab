# PubMedQA — Yes/Maybe Split

A filtered subset of the [PubMedQA](https://pubmedqa.github.io/) dataset containing only samples with a `final_decision` of **yes** or **maybe** (i.e. the **no** class is excluded). Used in Week 04 of the Applied Small Model AI Lab to study fine-tuning for biomedical question answering.

## Schema

| Column | Type | Description |
|---|---|---|
| `pubid` | int64 | PubMed article ID |
| `question` | string | Biomedical yes/no/maybe question |
| `long_answer` | string | Free-text abstractive answer from the abstract |
| `final_decision` | string | Label: `yes` or `maybe` |
| `context_full_text` | string | Concatenated context paragraphs used to answer the question |
| `context_labels` | List[string] | Per-paragraph relevance labels |
| `n_context_paragraphs` | int64 | Number of context paragraphs |
| `meshes` | List[string] | MeSH terms associated with the article |
| `n_meshes` | int64 | Number of MeSH terms |
| `reasoning_required_pred` | string | Prediction under reasoning-required setting |
| `reasoning_free_pred` | string | Prediction under reasoning-free setting |
| `question_len` | int64 | Token length of the question |
| `long_answer_len` | int64 | Token length of the long answer |
| `context_len` | int64 | Token length of the full context |

## Format

Stored as a HuggingFace `datasets` Arrow dataset (`data-00000-of-00001.arrow`). Load with:

```python
from datasets import load_from_disk

dataset = load_from_disk("datasets/dataset_pubmed_qa_yes_maybe")
print(dataset)
```

## Source

Original dataset: Jin et al., *PubMedQA: A Dataset for Biomedical Research Question Answering*, EMNLP 2019.  
HuggingFace hub: `pubmed_qa` (config: `pqa_labeled`).
