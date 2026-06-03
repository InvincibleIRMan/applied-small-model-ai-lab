# Datasets

This folder is the centralized data store for all labs across the series.

Each subfolder corresponds to the week that first introduced the dataset.
Datasets are shared across weeks when relevant.

## Structure

```
datasets/
├── week-02/      # Running your first local LLM
├── week-03/      # Chat templates
├── week-04/      # Why fine-tuning matters
├── week-05/      # Fine-tuning labs
├── week-06/      # Evaluation benchmarks
└── week-07/      # Deployment experiments
```

## Notes

- Large binary files (model weights, `.gguf`, `.safetensors`) are **not** committed to Git.
  Download instructions are provided in each week's README.
- CSV / JSONL files used in labs are committed when small enough ( < 10 MB).
- For larger datasets, a download script or HuggingFace dataset link is provided.
