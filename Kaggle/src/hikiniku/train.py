import os
import json  # JSONを扱うためにインポート
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from PIL import Image

def validate_images(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            try:
                with Image.open(file_path) as img:
                    img.verify()  # 画像が有効か確認
            except (IOError, SyntaxError) as e:
                print(f"Invalid image file: {file_path} - {e}")

validate_images("dataset/")

# 例として 224x224にリサイズし、学習データ/バリデーションデータに分割する想定
IMG_SIZE = (224, 224)
BATCH_SIZE = 32
EPOCHS = 5  # テスト用に少なめ

# データ拡張 + 正規化
train_datagen = ImageDataGenerator(
    rescale=1.0/255.0,
    validation_split=0.2,  # 20%をバリデーション
    rotation_range=20,
    horizontal_flip=True,
    zoom_range=0.2
)

train_generator = train_datagen.flow_from_directory(
    "dataset/",
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    subset='training'
)

val_generator = train_datagen.flow_from_directory(
    "dataset/",
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    subset='validation'
)

# クラス順の確認と保存
class_indices = train_generator.class_indices
print("クラスインデックス:", class_indices)

# クラス名リストを作成（インデックス順にソート）
CLASS_NAMES = [key for key, value in sorted(class_indices.items(), key=lambda item: item[1])]
print("クラス名リスト:", CLASS_NAMES)

# クラスインデックスをJSONファイルとして保存
with open('class_indices.json', 'w') as f:
    json.dump(class_indices, f)

# 転移学習の例: MobileNetV2
base_model = tf.keras.applications.MobileNetV2(
    input_shape=IMG_SIZE + (3,),
    include_top=False, 
    weights='imagenet'
)
base_model.trainable = False  # 転移学習でベースモデルは固定

model = tf.keras.Sequential([
    base_model,
    tf.keras.layers.GlobalAveragePooling2D(),
    tf.keras.layers.Dense(3, activation='softmax')  # 3種類(豚/牛/鳥)
])

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

model.fit(
    train_generator,
    epochs=EPOCHS,
    validation_data=val_generator
)

# モデル保存（推奨フォーマット）
model.save('model.keras')
