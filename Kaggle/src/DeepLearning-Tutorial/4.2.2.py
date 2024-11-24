import numpy as np
from sklearn import datasets
from sklearn import preprocessing
from tensorflow.keras.utils import to_categorical

# データセットのロード
iris = datasets.load_iris()
print(iris.data[:10])
print(iris.data.shape)
print(iris.target)

# データのスケーリング
scaler = preprocessing.StandardScaler()
scaler.fit(iris.data)
x = scaler.transform(iris.data)
print(x[:10])

# ラベルのone-hotエンコーディング
t = to_categorical(iris.target)
print(t[:10])


from sklearn.model_selection import train_test_split

x_train, x_test, t_train, t_test = train_test_split(x, t, train_size=0.75)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation

model= Sequential()
model.add(Dense(4096, input_dim=4))
model.add(Activation('tanh'))
model.add(Dense(4096))
model.add(Activation('tanh'))
model.add(Dense(3))
model.add(Activation('softmax'))
model.compile(optimizer='sgd', loss='categorical_crossentropy',metrics=['accuracy'])
print(model.summary())

history = model.fit(x_train,t_train,epochs=50,batch_size=4)

import matplotlib.pyplot as plt

hist_loss = history.history['loss']
hist_acc = history.history['accuracy']

plt.plot(np.arange(len(hist_loss)),hist_loss,label='loss')
plt.plot(np.arange(len(hist_acc)),hist_acc,label='accuryacy')
plt.legend()

plt.savefig('4.2.2.png')


loss, accuracy = model.evaluate(x_test, t_test)
print("誤差:",loss,"精度",accuracy)


y_test = model.predict(x_test)
print(y_test[:10])

from tensorflow.keras.models import load_model

model.save('model.h5')
load_model('model.h5')