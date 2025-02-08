import unittest
import numpy as np
class SquareTest(unittest.TestCase):
    def test_forward(self):
        x = Variable(np.array(3.0))
        y = square(x)
        expected = np.array(9.0)
        self.assertEqual(y.data, expected)

class Variable:
    def __init__(self,data):
        self.data = data

class Square:
    def __call__(self,input):
        x = input.data
        y = x ** 2;
        output = Variable(y)
        return output

def square(x):
    return Square()(x)

unittest.main()
