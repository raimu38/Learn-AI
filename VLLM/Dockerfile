# ─────────────────────────────────────────────
# Dockerfile for vLLM + Phi-4-Multimodal-Instruct
# (CUDA 12.4 + cuDNN 9, PyTorch 2.5.1)
# ─────────────────────────────────────────────

FROM pytorch/pytorch:2.5.1-cuda12.4-cudnn9-runtime

# 作業ディレクトリ
WORKDIR /app

# 必要なOSパッケージ
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      git \
      ffmpeg && \
    rm -rf /var/lib/apt/lists/*

# Pythonパッケージ
RUN pip install --no-cache-dir \
      vllm \
      transformers==4.48.2 \
      accelerate \
      fastapi \
      uvicorn[standard]

# GPUチェック用スクリプトを含める
COPY gpu_check.py .

# ポート開放
EXPOSE 8000

# デフォルトは vLLM サーバ起動
CMD ["vllm", "serve", "microsoft/Phi-4-multimodal-instruct", \
     "--trust-remote-code", \
     "--dtype", "auto", \
     "--max-model-len", "4096", \
     "--limit-mm-per-prompt", "audio=1,image=1", \
     "--port", "8000"]

