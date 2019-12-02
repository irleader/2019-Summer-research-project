from sklearn.preprocessing import normalize
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


x=np.arange(0,48)
dataset1 = pd.read_csv('/Users/jiajiaxu/PycharmProjects/JsonToCsv/f_pattern.csv',header=None)
X = dataset1.values[:,1]
X=X.reshape((-1,1))
normalized_X=normalize(X,axis=0)
normalized_X_24=normalized_X[0:48]



dataset2 = pd.read_csv('/Users/jiajiaxu/PycharmProjects/JsonToCsv/h_pattern.csv',header=None)
Y = dataset2.values[:,1]
Y=Y.reshape((-1,1))
normalized_Y=normalize(Y,axis=0)
normalized_Y_24=normalized_Y[0:48]

dataset2 = pd.read_csv('/Users/jiajiaxu/PycharmProjects/JsonToCsv/g_pattern.csv',header=None)
Z = dataset2.values[:,1]
Z=Z.reshape((-1,1))
normalized_Z=normalize(Z,axis=0)
normalized_Z_24=normalized_Z[0:48]

fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.plot(x,normalized_X_24,label="Homed Demand")
ax.plot(x,normalized_Y_24,label="Homeg Demand")
ax.plot(x,normalized_Z_24,label="Homeh Demand")
ax.legend()
ax.set_xlabel('hour')
ax.set_ylabel('load')



from math import *

def euclidean_distance(x,y):
    #return sqrt(sum(pow(a-b,2) for a,b in zip(x,y)))
    sum=0
    for a,b in zip(x,y):
        sum=sum+pow(a-b,2)
    return sqrt(sum/48)

    # sum=0
    # for i in range(len(x)):
    #     sum=sum+pow(x[i]-y[i],2)
    # return sqrt(sum)

result1=euclidean_distance(normalized_X_24,normalized_Y_24)
result2=euclidean_distance(normalized_X_24,normalized_Z_24)
result3=euclidean_distance(normalized_Y_24,normalized_Z_24)
print(result1)
print(result2)
print(result3)

#plt.show()