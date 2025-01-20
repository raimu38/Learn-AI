import pandas as pd


df = pd.DataFrame([['佐藤', 170, 60], ['田中', 160, 50], ['鈴木', 165, 58]])
df.columns = ["name","height","weight"]
# print(df)
# print(df.shape)
# print(df.columns, 1)

datasetA = {'name':["佐藤","加藤","伊藤","後藤","藤原"],"age":[12,43,32,65,33]}
pandasA = pd.DataFrame(datasetA)
print(pandasA)
N = 3
A = pd.DataFrame({'A':[1,2,3],'B':[2,3,4],'C':[x*2 for x in range(N)],'D':[x**2 for x in range(N)]})
print(A)



data = [10, 20, 30, 40]
s = pd.Series(data, index=['a', 'b', 'c', 'd'])

print(s)

dataA=[5,10,15,20]
indexA=['w','x','y','z']
SeriesA = pd.Series(dataA,indexA)
print('y :' + str(SeriesA['y']))


FruitsCollumn = ["Fruits","cost","kosu"]
N = 3
fruits = ["りんご","ばなな","オレンジ"]
cost = [100,150,200]
kosu = [50,30,20]
FruitsFrame = pd.DataFrame({{FruitsCollumn[j]: [fruits[i] for i in range(N)]} for j in range(3)})
print(FruitsFrame)