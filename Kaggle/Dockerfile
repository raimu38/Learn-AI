FROM python:3.11-slim

WORKDIR /app

# 必要なシステムライブラリをインストール
RUN apt-get update && apt-get install -y --no-install-recommends \
        vim \
        libgl1-mesa-glx \
        libglib2.0-0 \
        libsm6 \
        libxext6 \
        libgtk2.0-dev \
        libxrender1 \
        x11-apps \
        xvfb \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# requirements.txt をコピーして、Python パッケージをインストール
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのソースコードをコピー
COPY . /app

CMD ["bash"]
