# 最新のPythonイメージをベースに使用
FROM python:latest

# 作業ディレクトリを設定
WORKDIR /app

# 必要なパッケージのインストール（最小構成）
RUN apt-get update && apt-get install -y --no-install-recommends \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Pythonパッケージの依存関係用
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# プロジェクト全体をコンテナにコピー（srcを使用予定）
COPY . /app

# 必要に応じてデフォルトのCMDは変更可能
CMD ["bash"]

