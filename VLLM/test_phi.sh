#!/usr/bin/env bash
set -eux

ENDPOINT="http://localhost:8000/v1/chat/completions"

# ---- モデルロード完了待ち ----
echo "==> Waiting for vLLM server to be ready…"
until curl -s http://localhost:8000/v1/models >/dev/null 2>&1; do
  echo -n "."
  sleep 3
done
echo " ready!"

# ---- テキスト入力テスト ----
echo "==> Sending text prompt…"
curl "$ENDPOINT" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "model": "microsoft/Phi-4-multimodal-instruct",
    "messages": [
      {
        "role": "user",
        "content": "こんにちは、調子はどうですか？"
      }
    ]
  }'
echo

