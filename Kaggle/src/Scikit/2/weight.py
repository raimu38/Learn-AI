import numpy as np

# データの読み込み
npArray = np.loadtxt("in.csv", delimiter=",", dtype="float", skiprows=1)

# 説明変数と目的変数を分割
x = npArray[:, 1:3] # 説明変数 : すべての行、 1:3 インデックス1,2
y = npArray[:, 3:4].ravel()  # 目的変数

# 出力
print(f"説明変数:\n{x}\n")
print(f"目的変数:\n{y}")


from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3)

print(f"訓練データ説明変数{x_train}")
print(f"訓練デー目的変数{x_test}")
print(f"評価データ説明変数{y_train}")
print(f"評価データ目的変数{y_test}")

from sklearn import tree
#アルゴリズムを設定
clf = tree.DecisionTreeClassifier()
clf.fit(x_train, y_train)

# 学習済みモデルをテキスト形式で可視化
text_representation = tree.export_text(clf, feature_names=["Feature1", "Feature2"])
print(text_representation)

predict = clf.predict(x_test)
print(f"予測を出力\n{predict}")

from sklearn.metrics import accuracy_score
#モデルの評価
print(f"正解率を出力{accuracy_score(y_test,predict)}")