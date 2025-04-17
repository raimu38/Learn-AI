# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI(title="LLM A2A Agent API")

# 自然言語命令を受け取るリクエストボディのモデル
class CommandRequest(BaseModel):
    prompt: str

# エンドポイント例:
@app.post("/generate")
def generate_command(req: CommandRequest):
    # ここで LLM（例：Ollama）へ問い合わせる
    # OllamaのAPIサーバーは通常ポート11434で起動している前提
    #model = llama2, llama3, deepseek-r1
    ollama_url = "http://host.docker.internal:11434/api/generate"
    payload = {
        "model": "deepseek-r1",  # 必要に応じて変更
        "prompt": req.prompt,
        "stream": False
    }
    try:
        response = requests.post(ollama_url, json=payload)
        response.raise_for_status()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM問い合わせエラー: {e}")
    
    llm_result = response.json()  # 例: {"response": "{\"seconds\": 600}"}
    # ここで必要に応じ、さらにJSON整形処理を行う
    return {"llm_response": llm_result}

# 例えば、タイマー実行スクリプト等と連携するエンドポイントも追加可能
