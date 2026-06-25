# Special Lab 01 — Loop Engineering with Local Models

A hands-on tutorial that teaches **loop engineering** — the practice of designing autonomous AI systems that iterate toward a goal, rather than prompting a model once and accepting the result.

Based on: [Loop Engineering by Addy Osmani](https://addyosmani.com/blog/loop-engineering/)

---

## What Is Loop Engineering?

> *"Loop engineering is replacing yourself as the person who prompts the agent. You design the system that does it instead."*

| Traditional approach | Loop engineering |
|---|---|
| You write a prompt | You design a system that writes prompts |
| One model call → one output | Agents iterate until a goal condition is met |
| You judge the quality | A checker agent judges and feeds back |

---

## What You Will Learn

- The five core components of a loop: **Automations, Worktrees, Skills, Sub-agents, State**
- How to build a **Maker + Checker** sub-agent pattern
- How to manage **persistent state** across iterations
- How to define a **goal condition** that stops the loop
- How to **test hypotheses** by changing one variable and observing convergence speed

---

## Hardware Requirements

This lab runs a local GGUF model through `llama-server` and connects to it from the notebook via an OpenAI-compatible API.

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| GPU VRAM | 4 GB (partial offload, slow) | 8 GB+ (full offload) |
| System RAM | 8 GB | 16 GB+ |
| Disk space | ~6 GB (for a Q4 GGUF) | — |
| GPU | Any CUDA-capable NVIDIA GPU | — |

> **No GPU?** Set `N_GPU_LAYERS=0` in `start_server.sh` to run fully on CPU. Inference will be slow (30–60 s per response) but the notebook will still work.

### GPU Layers Guide

`--n-gpu-layers` controls how many transformer layers are offloaded to the GPU. More layers = faster inference, but more VRAM required. For a **Qwen3-8B Q4_K_XL** model (~5.2 GB on disk):

| Available VRAM | Recommended `N_GPU_LAYERS` | Notes |
|---|---|---|
| 4 GB | 15–20 | Partial offload; slow but usable |
| 6 GB | 28–32 | Most layers on GPU |
| 8 GB | 36 (all layers) | Full offload; best speed |
| 12 GB+ | 36 | Full offload with headroom for context |

If you see `out of memory` errors on startup, reduce `N_GPU_LAYERS` by 5 and try again.

---

## Setup Guide

### Step 1 — Install llama.cpp

You need the `llama-server` binary. The easiest path is a pre-built release:

1. Go to the [llama.cpp releases page](https://github.com/ggml-org/llama.cpp/releases)
2. Download the archive matching your platform (e.g., `llama-b<version>-bin-ubuntu-x64.zip` for Linux x86)
3. Extract it and note the path to the `llama-server` binary

Alternatively, build from source:

```bash
git clone https://github.com/ggml-org/llama.cpp
cd llama.cpp
cmake -B build -DGGML_CUDA=ON   # omit -DGGML_CUDA=ON if you have no GPU
cmake --build build --config Release -j$(nproc)
# binary is at build/bin/llama-server
```

### Step 2 — Download a GGUF model

The notebook is designed for **Qwen3-8B** (or similar 7–9B parameter models). Download a Q4 quantization for a good speed/quality balance:

```bash
pip install huggingface_hub
huggingface-cli download unsloth/Qwen3-8B-GGUF Qwen3-8B-UD-Q4_K_XL.gguf --local-dir ~/models/qwen3-8b
```

> Any instruction-tuned GGUF model in the 7B–13B range will work. Larger models need more VRAM.

### Step 3 — Configure `start_server.sh`

Open `start_server.sh` and edit the variables in the **CONFIGURATION** block:

```bash
LLAMA_SERVER="${LLAMA_SERVER_BIN:-/path/to/llama-server}"   # ← your binary path
LLAMA_MODEL="${LLAMA_MODEL:-/path/to/your-model.gguf}"      # ← your model path
N_GPU_LAYERS="${LLAMA_GPU_LAYERS:-35}"                       # ← adjust for your VRAM (see table above)
CTX_SIZE="${LLAMA_CTX_SIZE:-4096}"                           # ← leave at 4096
```

You can also set these as environment variables without editing the file:

```bash
LLAMA_SERVER_BIN=/usr/local/bin/llama-server \
LLAMA_MODEL=~/models/qwen3-8b/Qwen3-8B-UD-Q4_K_XL.gguf \
bash start_server.sh
```

### Step 4 — Start the server

**Run this from a terminal, not from inside the notebook:**

```bash
bash start_server.sh
```

Wait for:
```
Server ready at http://0.0.0.0:8080
```

To stop the server later:
```bash
bash start_server.sh stop
```

### Step 5 — Open the notebook

```bash
conda activate <your-env>   # or: source .venv/bin/activate
jupyter notebook Loop_Engineering.ipynb
```

Run cells top to bottom. The smoke test in **Step 2** of the notebook sends a single request to the server — if it prints a non-empty string, everything is working.

---

## Connecting via SSH

If Jupyter is running on a remote machine, forward the ports when you connect:

```bash
ssh -L 8080:localhost:8080 -L 8888:localhost:8888 user@your-server-ip
```

Then open `http://localhost:8888` in your local browser as usual.

> The server must be started from the host terminal, not from inside the notebook, because the Jupyter kernel cannot easily manage background processes across a port-forwarded session.

---

## Files

| File | Purpose |
|---|---|
| `Loop_Engineering.ipynb` | Main tutorial notebook |
| `start_server.sh` | Launches the llama.cpp inference server in the background |
| `figures/` | Diagrams used in the notebook |

---

## Notebook Structure

| Section | What It Covers |
|---|---|
| Step 0 | Prerequisites and SSH setup |
| Step 1 | Server health check |
| Step 2 | OpenAI-compatible client wrapper |
| Step 3 | Baseline: single-pass generation (the control) |
| Step 4 | Skills: reusable system prompts (codified knowledge) |
| Step 5 | State management: JSON file that persists across iterations |
| Step 6 | Sub-agents: Maker (T=0.8) and Checker (T=0.1) |
| Step 7 | The Loop: runs until goal score is met or max iterations reached |
| Step 8 | Baseline vs. loop comparison |
| Step 9 | Score progression chart |
| Step 10 | Inspect the persistent state file |
| Step 11 | Hypothesis experiments (task, checker strictness, temperature) |
| Step 12 | Server shutdown |

---

## Key Concepts Demonstrated

### The Goal Primitive
The loop exits only when a condition is **actually true** — not after a fixed number of steps:
```python
if score >= GOAL_SCORE:
    break
```

### The Maker / Checker Split
> *"The model that wrote the code is way too nice grading its own homework."*

Two agents call the same model with different system prompts and temperatures:
- **Maker** (T=0.8) — creative, generative
- **Checker** (T=0.1) — critical, structured

### State on Disk
> *"The model forgets everything between runs so the memory has to be on disk."*

Every iteration writes its output, feedback, and score to `/tmp/loop_state.json`. The loop can resume after a crash without re-deriving context.

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `Error: llama-server binary not found` | Path not set | Edit `LLAMA_SERVER` in `start_server.sh` |
| `Error: model file not found` | Path not set | Edit `LLAMA_MODEL` in `start_server.sh` |
| Health check fails (`Connection refused`) | Server not started | Run `bash start_server.sh` from the terminal |
| Server exits with `out of memory` | Too many GPU layers | Reduce `N_GPU_LAYERS` by 5 and retry |
| Notebook prints empty strings | Qwen3 thinking mode overflow | Already fixed: server runs with `-rea off` |
| All checker criteria FAIL | Model output was empty | Restart kernel, re-run after smoke test passes |
| Server exits with `libnccl` error | NCCL library not on path | Set `NCCL_LIB` to the directory containing `libnccl.so.2` |

### Note on Qwen3 thinking mode

Qwen3 models generate a verbose chain-of-thought block (`<think>...</think>`) before every answer. On some configurations, thinking alone consumes thousands of tokens, leaving nothing for the actual response.

`start_server.sh` disables reasoning at the server level with three flags:

```bash
--reasoning-format deepseek   # route thinking to reasoning_content, keep content clean
--reasoning-budget 0          # cap thinking at 0 tokens
-rea off                      # explicitly disable reasoning
```

If you switch to a model that does not support these flags, remove them from the script.

---

## Going Further

- Replace the JSON state file with a **SQLite database** for multi-loop tracking
- Add an **Explorer sub-agent** that searches previous iterations before the maker drafts
- Use `--parallel N` in `llama-server` to run maker and checker concurrently
- Swap in a code-specialized model (e.g., Qwen3-Coder) for code generation loops
- Wire the loop to a real task source: a CSV of prompts, GitHub issues, or a dataset

---

## Credits

Tutorial design and implementation based on concepts from
[Loop Engineering — Addy Osmani](https://addyosmani.com/blog/loop-engineering/)
