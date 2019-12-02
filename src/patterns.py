import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import *

a=pd.read_csv('/Users/jiajiaxu/PycharmProjects/JsonToCsv/a_extracted.csv',header=None)
b=pd.read_csv('/Users/jiajiaxu/PycharmProjects/JsonToCsv/b_extracted.csv',header=None)
c=pd.read_csv('/Users/jiajiaxu/PycharmProjects/JsonToCsv/c_extracted.csv',header=None)
d=pd.read_csv('/Users/jiajiaxu/PycharmProjects/JsonToCsv/d_extracted.csv',header=None)
e=pd.read_csv('/Users/jiajiaxu/PycharmProjects/JsonToCsv/e_extracted.csv',header=None)
f=pd.read_csv('/Users/jiajiaxu/PycharmProjects/JsonToCsv/f_extracted.csv',header=None)
g=pd.read_csv('/Users/jiajiaxu/PycharmProjects/JsonToCsv/g_extracted.csv',header=None)
h=pd.read_csv('/Users/jiajiaxu/PycharmProjects/JsonToCsv/h_extracted.csv',header=None)


a=a.values
b=b.values
c=c.values
d=d.values
e=e.values
f=f.values
g=g.values
h=h.values


value=h # change this from a to h to get different extracted data for pattern a to h
X=np.arange(0.5, 23, 0.5)
result=np.zeros((45))
Y= value[:, 0]
lst= [[0 for j in range(len(Y))] for i in range(len(X))]
ary=np.zeros((len(X), len(Y)))

for x in X:
    lst[list(X).index(x)]= Y - x

# for x in Xa:
#     ary[list(Xa).index(x)]=Ya-x

for j in range(len(X)):
    maximum = - inf
    minimum = inf
    for i in lst[j]:
        if i>0:
            if i<minimum:
                minimum=i
        if i<0:
            if i>maximum:
                maximum=i
    minimum= X[j] + minimum
    maximum= X[j] + maximum
    index1=list(Y).index(maximum)
    index2=list(Y).index(minimum)
    index2=list(Y).index(minimum)
    result[j]=(value[index1][1]+value[index2][1])/2

R=np.zeros((48))
R[1:46]=result
v=R[45]-R[1]
if v>=0:
    R[0]=R[1]+1/4*v
    R[47]=R[1]+1/2*v
    R[46]=R[1]+3/4*v
if v<0:
    R[0]=R[45]-3/4*v
    R[47]=R[45]-1/2*v
    R[46]=R[45]-1/4*v
    


t=np.arange(0,24,0.5)
fig=plt.plot(X,result)
fig2=plt.plot(t,R)


R=pd.DataFrame(R)

# change this from a to h to generate different pattern data for a to h
R.to_csv('%s_pattern.csv'%'h',header=None)

plt.show()