# Applied Small Models AI Lab

> A hands-on journey into Small Language Models — from running your first local model to fine-tuning and deployment with llama.cpp.

[![YouTube](https://img.shields.io/badge/YouTube-Applied_SLM_Lab-red?logo=youtube)](https://youtube.com/@AppliedSLMLab)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Substack](https://img.shields.io/badge/Substack-Applied_SLM_Lab-orange?logo=substack&logoColor=white)](https://appliedslmlab.substack.com)


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
| 01 | Welcome to Applied Small Models AI Lab | Jun 8, 2026 | [Watch](https://youtube.com) | [Read](https://substack.com) | — |
| 02 | Hello Small Language Models: Running Your First Local LLM | Jun 15, 2026 | Coming Soon | Coming Soon | Coming Soon |
| 03 | Mastering Chat Templates: The Hidden Language of LLMs | Jun 22, 2026 | Coming Soon | Coming Soon | Coming Soon |
| 04 | Why Fine-Tuning Matters: Beyond Prompt Engineering | Jun 29, 2026 | Coming Soon | Coming Soon | Coming Soon |
| 05 | Fine-Tuning Small Language Models for Specialized Tasks | Jul 6, 2026 | Coming Soon | Coming Soon | Coming Soon |
| 06 | Deploying Small Language Models with llama.cpp | Jul 13, 2026 | Coming Soon | Coming Soon | Coming Soon |

> **Links are updated every Monday on release day.**
> Star the repo to get notified automatically.

---

## Release Status

| Week | Status |
|------|--------|
| Week 01 – Welcome | Released Jun 8, 2026 |
| Week 02 – Hello sLM | Coming Soon |
| Week 03 – Chat Templates | Coming Soon |
| Week 04 – Why Fine-Tuning | Coming Soon |
| Week 05 – Fine-Tuning | Coming Soon |
| Week 06 – llama.cpp Deployment | Coming Soon |

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
└── week-06-llama-cpp-deployment/
    ├── week06_llama_cpp.ipynb
    ├── code/
    └── assets/
```

---

## Getting Started

### Prerequisites

- Python 3.10+
- [uv](https://docs.astral.sh/uv/) or `pip` for package management
- CUDA GPU recommended for fine-tuning weeks; CPU is fine for inference weeks

### Install

```bash
git clone https://github.com/your-username/applied-small-models-ai-lab.git
cd applied-small-models-ai-lab

# create a virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# install dependencies for the week you're working on
pip install -r week-02-hello-slm/code/requirements.txt
```

---

## How to Follow Along

1. **Watch** the YouTube video for the conceptual overview.
2. **Read** the Substack article for depth and context.
3. **Open** the notebook in `week-XX/` and run the cells.
4. **Experiment** — tweak the code, break things, rebuild.
5. **Share** your results or questions in the Discussions tab.

---

## Future Seasons (Planned)

| Season | Focus |
|--------|-------|
| Season 2 | Quantization & Model Compression |
| Season 3 | Retrieval-Augmented Generation (RAG) |
| Season 4 | Function Calling & Tool Use |
| Season 5 | Agentic AI with Small Models |
| Season 6 | Vision Language Models |
| Season 7 | Small Language Models for Cybersecurity |

---

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

## Contact

- **YouTube:** [Applied Small Models AI Lab](https://youtube.com)
- **Substack:** [Applied Small Models AI Lab](https://substack.com)
- **GitHub Discussions:** Use the Discussions tab for questions
- **Email:** sadegh.pub@gmail.com

---

*If this series helps you, consider starring the repo — it helps others find it.*
