#!/usr/bin/env bash
# Run this ONCE from your terminal before opening the notebook.
# The server stays running in the background until you stop it.
#
# Usage:
#   bash start_server.sh           # start on port 8080 (default)
#   bash start_server.sh 9090      # use a different port
#   bash start_server.sh stop      # kill any running instance
#
# You can also override any variable without editing this file:
#   LLAMA_MODEL=/path/to/model.gguf bash start_server.sh

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURATION — edit these four values to match your setup
# ─────────────────────────────────────────────────────────────────────────────

# Path to the compiled llama-server binary.
# Get a pre-built release from: https://github.com/ggml-org/llama.cpp/releases
# Or build from source: https://github.com/ggml-org/llama.cpp#build
LLAMA_SERVER="${LLAMA_SERVER_BIN:-/path/to/llama-server}"

# Path to a GGUF model file (Qwen3-8B or similar recommended).
# Download from Hugging Face, e.g.:
#   huggingface-cli download unsloth/Qwen3-8B-GGUF Qwen3-8B-UD-Q4_K_XL.gguf
LLAMA_MODEL="${LLAMA_MODEL:-/path/to/your-model.gguf}"

# Number of transformer layers to offload to GPU.
# Higher = faster inference but more VRAM required.
# See the README for a VRAM/layers guide.
N_GPU_LAYERS="${LLAMA_GPU_LAYERS:-35}"

# Context window size in tokens.
# 4096 is sufficient for all notebook exercises.
CTX_SIZE="${LLAMA_CTX_SIZE:-4096}"

# (Optional) Path to the NCCL shared library directory.
# Only needed on some multi-GPU NVIDIA setups. Leave empty if not required.
NCCL_LIB="${NCCL_LIB:-}"

# ─────────────────────────────────────────────────────────────────────────────

PORT="${1:-8080}"
LOG="/tmp/llama_server.log"

# --- stop command ---
if [[ "$1" == "stop" ]]; then
    echo "Stopping llama-server..."
    pkill -f "llama-server" && echo "Stopped." || echo "No running instance found."
    exit 0
fi

# --- validate paths ---
if [[ ! -f "$LLAMA_SERVER" ]]; then
    echo "Error: llama-server binary not found at: $LLAMA_SERVER"
    echo "Edit LLAMA_SERVER in this script or set the LLAMA_SERVER_BIN environment variable."
    exit 1
fi

if [[ ! -f "$LLAMA_MODEL" ]]; then
    echo "Error: model file not found at: $LLAMA_MODEL"
    echo "Edit LLAMA_MODEL in this script or set the LLAMA_MODEL environment variable."
    exit 1
fi

# --- kill any previous instance on the same port ---
pkill -f "llama-server.*${PORT}" 2>/dev/null && echo "Killed previous instance." && sleep 1

# --- optionally extend LD_LIBRARY_PATH for NCCL ---
if [[ -n "$NCCL_LIB" ]]; then
    export LD_LIBRARY_PATH="${NCCL_LIB}:${LD_LIBRARY_PATH}"
fi

# --- start server ---
nohup "${LLAMA_SERVER}" \
    --model              "${LLAMA_MODEL}" \
    --port               "${PORT}" \
    --host               "0.0.0.0" \
    --ctx-size           "${CTX_SIZE}" \
    --n-gpu-layers       "${N_GPU_LAYERS}" \
    --no-mmap \
    -fit                 off \
    --reasoning-format   deepseek \
    --reasoning-budget   0 \
    -rea                 off \
    > "${LOG}" 2>&1 &

SERVER_PID=$!
echo "llama-server started (PID ${SERVER_PID}) on port ${PORT}"
echo "Log: ${LOG}"
echo ""
echo "Waiting for model to load..."
for i in $(seq 1 12); do
    sleep 3
    STATUS=$(curl -s "http://localhost:${PORT}/health" 2>/dev/null \
        | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('status','?'))" 2>/dev/null)
    if [[ "$STATUS" == "ok" ]]; then
        echo "Server ready at http://0.0.0.0:${PORT}"
        echo "Now open the notebook — it will connect automatically."
        exit 0
    fi
    echo "  ... still loading (attempt ${i}/12)"
done

echo ""
echo "Server did not respond after 36 s. Check ${LOG} for details."
exit 1
