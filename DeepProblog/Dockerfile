FROM python:3.9-slim

# 必要なパッケージ
RUN apt-get update && apt-get install -y \
    git build-essential cmake swig libprotobuf-dev && \
    rm -rf /var/lib/apt/lists/*

# DeepProbLog クローン＆インストール
RUN git clone https://github.com/ML-KULeuven/deepproblog.git /opt/deepproblog && \
    pip install torch torchvision && \
    pip install -e /opt/deepproblog

WORKDIR /workspace
CMD ["/bin/bash"]
