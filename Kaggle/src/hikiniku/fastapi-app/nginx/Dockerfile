FROM nginx:latest

# 証明書ファイルをコンテナにコピー
COPY ssl/fullchain.pem /etc/nginx/ssl/fullchain.pem
COPY ssl/privkey.pem /etc/nginx/ssl/privkey.pem

# Nginx 設定ファイルをコンテナにコピー
COPY nginx.conf /etc/nginx/nginx.conf

# ポート 80 と 443 を公開
EXPOSE 80 443

