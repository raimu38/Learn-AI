import numpy as np
from sklearn import datasets

iris = datasets.load_iris()
# print(iris.data[:10])
# print(iris.data.shape)
# print(iris.target)

from sklearn import preprocessing
from tensorflow.keras.utils import to_categorical

scaler = preprocessing.StandardScaler()#scalerオブジェクトを生成
scaler.fit(iris.data) #iris.dataから 計算してscalerオブジェクトの平均値、　標準偏差を更新
x = scaler.transform(iris.data)#更新されたので 標準化を実行できる。
# print(x[:10])


# ラベルのone-hotエンコーディング
t = to_categorical(iris.target)
# print(t[:10])

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,t,train_size = 0.75)

print(x_train[:5])
print(x_test[:5])
print(y_test[:5])
print(y_train[:5])

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation

