import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

datasets=pd.read_csv('/Users/jiajiaxu/PycharmProjects/JsonToCsv/optimal_solution1.csv')
t=range(406)

X=datasets.values

x=X[:,7]
x1=X[:,5]
x2=X[:,6]

fig,axes=plt.subplots(1,1)


axes.plot(t,x,label='cost reduction by direct connection based on standalone (%)')
#axes.plot(t,x1)
#axes.plot(t,x2)
axes.set_xlabel('pair')
axes.set_ylabel('cost reduction percentage')
plt.legend()

fig,axes1=plt.subplots(3,1)
axes1[0].hist(x1)
axes1[1].hist(x2)
axes1[2].hist(x)

plt.show()
