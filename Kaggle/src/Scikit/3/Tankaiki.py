import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

df = pd.DataFrame('https://archive.ics.uci.edu/ml/machine-learing-database/housing.data', header=None, sep='\s+')

#P68
