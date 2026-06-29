# Applied Small Models AI Lab

> A hands-on journey into Small Language Models — from running your first local model to fine-tuning and deployment with llama.cpp.


[![YouTube](https://img.shields.io/badge/YouTube-Applied_SM_Lab-red?logo=youtube)](https://www.youtube.com/@appliedsmlab)
[![Substack](https://img.shields.io/badge/Substack-Applied_SM_Lab-orange?logo=substack&logoColor=white)](https://smallmodelslab.substack.com/)
[![Website](https://img.shields.io/badge/🌐_Website-sadegh--mh.com-green)](https://sadegh-mh.com)


---

## What Is This?

**Applied Small Models AI Lab** is a weekly educational series that helps practitioners, students, researchers, and engineers move **beyond prompting and APIs** and gain a practical understanding of how Small Language Models (sLMs) work under the hood.

Each week combines a YouTube video, a Substack article, and hands-on Jupyter notebooks with runnable code — so you can follow along, experiment, and build real intuition.

---

## Who Is This For?

| Background | What you'll get |
|---|---|
| ML practitioners | Hands-on labs that go deeper than API wrappers |
| Students & researchers | Structured curriculum with code and theory |
| Software engineers | Step-by-step guides from zero to fine-tuning |
| Curious builders | A no-fluff, no-hype path into sLMs |

---

## Learning Objectives

By the end of Season 1 you will be able to:

- Run open-source language models entirely on your own hardware
- Understand tokenization, inference, and chat templates at the code level
- Fine-tune a small language model for a specialized task
- Deploy a quantized model locally using `llama.cpp`
- Read and understand the architecture choices that make sLMs practical

---

## Course Roadmap

| Week | Topic | Release Date | YouTube | Substack | Notebook |
|------|-------|-------------|---------|----------|----------|
| 01 | Welcome to Applied Small Models AI Lab | Jun 8, 2026 | [Watch](https://www.youtube.com/channel/UCvTucZbIhpArq_61DcQJG2w) | [Read](https://smallmodelslab.substack.com/p/welcome-to-the-applied-small-models) | — |
| 02 | Hello Small Language Models: Running Your First Local LLM | Jun 15, 2026 | [Watch](https://www.youtube.com/watch?v=B_fz1uYU28o) | [Read](https://smallmodelslab.substack.com/p/lab1-hello-small-language-models) | [Hands-on-Notebook](https://github.com/InvincibleIRMan/applied-small-model-ai-lab/tree/main/week-02-hello-slm/code) |
| 03 | Mastering Chat Templates: The Hidden Language of LLMs | Jun 22, 2026 | [Watch](https://youtu.be/B4p_ERF6oUw) | [Read](https://smallmodelslab.substack.com/p/lab2-chat-templates-talking-to-language) | [Hands-on-Notebook](https://github.com/InvincibleIRMan/applied-small-model-ai-lab/blob/main/week-03-chat-templates/code/Chat_Templates_Tutorial.ipynb) |
| 04 | Why Fine-Tuning Matters: Beyond Prompt Engineering | Jun 29, 2026 | — | — | [Hands-on-Notebook](https://github.com/InvincibleIRMan/applied-small-model-ai-lab/blob/main/week-04-why-fine-tuning-matters/code/why_fine_tunning-matters.ipynb) |
| 05 | Fine-Tuning Small Language Models for Specialized Tasks | Jul 6, 2026 | — | — | — |
| 06 | Deploying Small Language Models with llama.cpp | Jul 13, 2026 | — | — | — |

> **Links are updated every Monday on release day.**
> Star the repo to get notified automatically.

### Special Labs

Bonus content released outside the weekly schedule — standalone deep-dives, timely topics, and community-requested labs. These are independent of the 6-week curriculum and can be followed in any order.

| # | Topic | Release Date | YouTube | Substack | Notebook |
|---|-------|-------------|---------|----------|----------|
| 01 | Loop Engineering with Local Qwen Models | Jun 25, 2026 | — | — | [Hands-on Notebook](special_labs/special-01-loop-engineering/Loop_Engineering.ipynb) |

---

## Repository Structure

```
applied-small-models-ai-lab/
│
├── README.md                          ← You are here
├── LICENSE
├── .gitignore
│
├── assets/                            ← Repo-level images and banners
├── docs/                              ← Additional guides and references
├── datasets/                          ← Centralized datasets for all labs
│
├── week-01-welcome/
│
├── week-02-hello-slm/
│   ├── week02_hello_slm.ipynb     ← lab notebook
│   ├── code/                      ← supporting scripts
│   └── assets/                    ← images and diagrams
│
├── week-03-chat-templates/
│   ├── week03_chat_templates.ipynb
│   ├── code/
│   └── assets/
│
├── week-04-why-fine-tuning-matters/
│   ├── week04_why_finetuning.ipynb
│   ├── code/
│   └── assets/
│
├── week-05-fine-tuning/
│   ├── week05_fine_tuning.ipynb
│   ├── code/
│   └── assets/
│
├── week-06-llama-cpp-deployment/
│   ├── week06_llama_cpp.ipynb
│   ├── code/
│   └── assets/
│
└── special_labs/                      ← bonus lessons released outside the main schedule
    └── special-NN-topic-name/
        ├── README.md              ← setup and usage guide for this lesson
        ├── figures/               ← images and diagrams
        └── *.ipynb                ← hands-on notebook
```

---

## Getting Started

### Prerequisites

- Python 3.10+
- [uv](https://docs.astral.sh/uv/) or `pip` for package management
- A CUDA-enabled NVIDIA GPU is ESSENTIAL for running the labs efficiently. If you do not have access to one, you can use Google Colab, which offers free access to NVIDIA T4 GPUs and is sufficient for most course exercises.

---

## How to Follow Along

1. **Watch** the YouTube video for the conceptual overview.
2. **Read** the Substack article for depth and context.
3. **Open** the notebook in `week-XX/` and run the cells.
4. **Experiment** — tweak the code, break things, rebuild.
5. **Share** your results or questions in the Discussions tab.


## Contributing

Contributions, corrections, and improvements are welcome.

1. Fork the repository
2. Create a branch: `git checkout -b fix/week-02-typo`
3. Make your changes and commit: `git commit -m "fix: correct tokenizer example in week 02"`
4. Open a pull request with a clear description

Please keep PRs focused — one fix or improvement per PR.

---

## License

This project is licensed under the [MIT License](LICENSE).
You are free to use, adapt, and share the code with attribution.

---

*If this series helps you, consider starring the repo — it helps others find it.*
