import numpy as np

class Variable:
    def __init__(self, data):
        self.data = data

class Function:
    def __call__(self, input):
        x = input.data
        y = self.forward(x)
        output = Variable(y)
        return output

    def forward(self, x):
        raise NotImplementedError()
    
class Square(Function):
    def forward(self,x):
        return x ** 2

class Exp(Function):
    def forward(self,x):
        return np.exp(x)
    

def numerical_diff(f, x , eps=1e-4):
    x0 = Variable(x.data - eps)
    x1 = Variable(x.data + eps)
    y0 = f(x0)
    y1 = f(x1)
    return (y1.data - y0.data)/(2*eps)


f = Square()
x = Variable(np.array(2.0))
diff = numerical_diff(f,x)
print(diff)

def f(x):
    A = Square()
    B = Exp()
    C = Square()
    return C(B(A(x)))
x = Variable(0.5)
dy = numerical_diff(f,x)
print(dy)

def f(x):
    return x ** 3
def numericla_diff(f, x , eps = 1e-4):
    x1 = Variable(x.data + eps)
    x2 = Variable(x.data  - eps)
    y1 = f(x1)
    y2 = f(x2)
    dy = (y1 - y2)/(2*eps)
    return Variable(dy)

S = Square()
E = Exp()
x = Variable(np.array(5.0))
f = E(S(S(E(x))))

dy = numerical_diff(f, 2.0)
print(dy)
