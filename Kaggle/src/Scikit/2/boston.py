from sklearn.datasets import load_breast_cancer
boston = load_boston()
print(boston.DESCR)

import pandas as pd

df = pd.DataFrame(boston.data, columns=boston.feature_names)
df['MEDV'] = boston.target
x = df.RM.to_frame()
y = df.MEDV
print(x)
print(y)