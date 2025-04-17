from fastapi import FastAPI, Request
from pydantic import BaseModel
import requests

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str
    model: str = "llama2"

@app.post("/generate")
def generate_text(data: PromptRequest):
    ollama_url = "http://host.docker.internal:11434/api/generate"
    
    payload = {
        "model": data.model,
        "prompt": data.prompt,
        "stream": False
    }

    response = requests.post(ollama_url, json=payload)
    result = response.json()
    return {"response": result.get("response")}

