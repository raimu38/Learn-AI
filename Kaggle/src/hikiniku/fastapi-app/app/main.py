
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, File, UploadFile
import uvicorn
import tensorflow as tf
import numpy as np
from PIL import Image
from fastapi.middleware.cors import CORSMiddleware  

app = FastAPI()
# CORS 設定
origins = [
  #  "http://localhost:3000",            # React アプリケーションのローカル開発サーバー
  #  "http://162.43.15.121:3000",        # 必要に応じて他のオリジンを追加
    "https://satokenai.com",  
    "https://www.satokenai.com",# 本番環境のドメインを追加
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,               # 許可するオリジン
    allow_credentials=True,
    allow_methods=["*"],                 # 許可するHTTPメソッド
    allow_headers=["*"],                 # 許可するHTTPヘッダー
)

templates = Jinja2Templates(directory="templates")

# モデル読み込み
MODEL_PATH = "model.keras"
model = tf.keras.models.load_model(MODEL_PATH)

CLASS_NAMES = ['beef', 'chicken', 'pork']


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html",{"request": request})

@app.get("/about", response_class=HTMLResponse)
async def about_page(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

@app.post("/predict")
async def predict_meat(file: UploadFile = File(...)):
    # 画像読み込み
    image = Image.open(file.file).resize((224, 224))
    img_array = np.array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    predictions = model.predict(img_array)[0]  # [0]で1次元配列に
    # 例: {"pork": 0.7, "beef": 0.2, "chicken": 0.1} のように返す
    result = {CLASS_NAMES[i]: float(predictions[i]) for i in range(len(CLASS_NAMES))}
    return result
