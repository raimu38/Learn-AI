from problog.program import PrologFile
from problog import get_evaluatable
from deepproblog import Model, Network
from deepproblog.engines import ExactEngine
from deepproblog.examples.MNIST.data import AdditionDataset
from deepproblog.evaluate import get_accuracy
from deepproblog.training import train_model

# 1. 論理プログラム読み込み（ProbLog API使用）
program = PrologFile("addition.problog")

# 2. ニューラルネットワーク部分を定義
net = Network("mnist", "mnist_model.pth", batching=True)
net.optimizer = "adam"

# 3. モデル構築
model = Model(program, [net])
model.set_engine(ExactEngine(model), cache=True)

# 4. データセット
train_set = AdditionDataset(train=True, size=100)
test_set = AdditionDataset(train=False, size=20)

# 5. 学習実行
train_model(model, train_set, epochs=5)

# 6. 精度評価
accuracy = get_accuracy(model, test_set)
print(f"Test accuracy: {accuracy * 100:.2f}%")

