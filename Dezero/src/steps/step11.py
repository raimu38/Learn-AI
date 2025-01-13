import numpy as np

class Function:
    def __call__(self, inputs):
        xs = [x.data for x in  inputs]
        ys = self.forward(xs)
        outputs =  [Variable(as_array(y)) for y in ys]

        for output in outputs:
            output.set_creator(self)
        self.inputs = inputs
        self.outputs = outputs
        return outputs
    
    def forward(self, xs):
        raise NotImplementedError()
    
    def backward(self, gys):
        raise NotImplementedError()
    


class Variable:
    def __init__(self,data):
        self.data = data

class Add(Function):
    def forward(self, xs):
        x0, x1 = xs
        y = x0 + x1
        return (y,)
    

xs = [Variable(np.array(2)), Variable(np.array(3))]
f = Add()
ys =f(xs)
y =ys[0]
print(y.data)