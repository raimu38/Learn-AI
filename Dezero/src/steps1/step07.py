import numpy as np


class Variable:
    def __init__(self, data):
        if data is not None:
            if not isinstance(data, np.ndarray):
                raise TypeError(f'{type(data) } is not suppoted.')
        self.data = data
        self.grad = None
        self.creater = None

    def set_creater(self,func):
        self.creater =func

    def backward(self):
        f = self.creater
        if f is not None:
            x = f.input
            x.grad = f.backward(self.grad)
            x.backward()

class Function:
    def __call__(self,input):
        x = input.data
        y = self.forward(x)

        output = Variable(y)
        output.set_creater(self)
        self.input = input
        self.output= output
        return output


x = Variable(np.array(1.0))
x = Variable(None)
x = Variable(np.array(5.000))