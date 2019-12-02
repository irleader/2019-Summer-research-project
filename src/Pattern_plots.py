import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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


fig,ax=plt.subplots(4,2,sharex=True,sharey=True)
ax[0,0].plot(a[:,0],a[:,1])
ax[0,1].plot(b[:,0],b[:,1])

ax[1,0].plot(c[:,0],c[:,1])
ax[1,1].plot(d[:,0],d[:,1])

ax[2,0].plot(e[:,0],e[:,1])
ax[2,1].plot(f[:,0],f[:,1])

ax[3,0].plot(g[:,0],g[:,1])
ax[3,1].plot(h[:,0],h[:,1])

plt.tight_layout()
plt.show()





