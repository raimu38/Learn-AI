FROM python:3.11-slim

WORKDIR /app

# 必要なライブラリをインストール
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        vim \
        libgl1-mesa-glx \
        libglib2.0-0 \
        libsm6 \
        libxext6 \
        libxrender1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD ["bash"]
