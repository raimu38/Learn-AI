import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(100,1)
x = x * 2  - 1

y = 4*x**3 - 3*x**2 + 2*x - 1

y += np.random.randn(100,1)

x_train = x[:30]
y_train = y[:30]

x_test = x[30:]
y_test = y[30:]

# plt.subplot(2,2,1)
# plt.scatter(x,y,marker='+')
# plt.title('all')

# plt.subplot(2,2,2)
# plt.scatter(x_train, y_train, marker="+")
# plt.title('train')

# plt.subplot(2,2,3)
# plt.scatter(x_test, y_test, marker="+")
# plt.title('test')

# plt.tight_layout()
# plt.savefig('result.png')


from sklearn import linear_model

X_TRAIN = np.c_[ *[x_train**i for i in range(9,-1,-1)]]
# print(X_TRAIN)
model = linear_model.Ridge()
# model = linear_model.LinearRegression()
model.fit(X_TRAIN,y_train)

print(model.coef_)
print(model.intercept_)
print(model.score(X_TRAIN,y_train))

plt.scatter(x_train,y_train,marker='+')
plt.scatter(x_train, model.predict(X_TRAIN))
plt.savefig('result.png')

X_TEST = np.c_[*[x_test**i for i in range(9,-1,-1)]]
print(model.score(X_TEST,y_test))
plt.scatter(x_test, y_test, marker="*")
plt.scatter(x_test,model.predict(X_TEST))
plt.savefig('result2.png')