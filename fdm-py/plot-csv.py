import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
import numpy as np

data = pd.read_csv('decay-cpp.csv')

name =[]
for col in data.columns:
    name.append(col)

print(name[0])

tminus = data[name[0]].to_numpy()
fx = data[name[1]].to_numpy()
#print(tminus)
#print(fx)
#print(fx.shape)


fig, ax = plt.subplots()
ax.plot(tminus,fx)
ax.set(xlabel='time', ylabel='f(x)',title='Peak decay')
ax.grid()
fig.savefig('decay-cpp.png')
plt.show()
