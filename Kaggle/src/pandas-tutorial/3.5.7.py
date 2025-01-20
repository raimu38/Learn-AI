import pandas as pd
import numpy as np


a = pd.Series([60, 80, 70, 50, 30], index=["Japanese","English","Math","Science","History"])
print(type(a))
print(a)

a = pd.Series({"Japanese":60,"Math":90,"History":20,"English":30})
print(type(a))
print(a)


a = pd.Series([60, 80, 70, 50, 30], index=["Japanese","English","Math","Science","History"])
print(a[2])
print(a['English'])
b = pd.Series([50],index=["Physics"])
b =  pd.concat([b,a])
print(b)


a = pd.DataFrame([[80, 60, 70, True], [90, 75, 85, False], [55, 65, 70, True], [45, 50, 60, False],
                  [70, 80, 75, True], [60, 70, 65, False], [85, 95, 90, True], [50, 55, 50, False]],
                 columns=['Math', 'Science', 'English', 'Passed'])

print(a)

a.index = ["Taro","Jiro","Saburo","Takumi","Nanako","Hanako","Yoshiro","Ideco"]
print(a)

print(a.shape)


print(a.head())
print(a.tail())


print(a.head(2))

print(a.tail(2))

print(a.describe())

tr = a.loc["Taro", :]
print(type(tr))
print(tr)

ma = a.loc[:,"Science"]
print(ma)

r = a.iloc[2:, :4]
print(r)


a = a.sort_values(by="Math",ascending=True)
print(a)