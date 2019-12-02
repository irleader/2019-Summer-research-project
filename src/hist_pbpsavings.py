import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

datasets0=pd.read_csv('/Users/jiajiaxu/PycharmProjects/JsonToCsv/paybackperiod_savings/egalitarian_ampetusenergypod.csv')
X0=datasets0.values
d1=X0[:,6]
d2=X0[:,8]
X=[]

for j in range(len(d1)):
    if d1[j]>0 and d2[j]>0:
        X.append(X0[j,:])
    else:
        X.append([0,0,0,0,0,0,0,0,0])
X=np.array(X)

r10= X[:, 3]
r20= X[:, 4]
r0=np.concatenate((r10,r20))*100
Y0=[] #positive results
for i in range(len(r10)):
    if r10[i]>=0 and r20[i]>=0:
        Y0.append(X[i, :])
Y0=np.array(Y0)

result10=Y0[:,3]
result20=Y0[:,4]
result0=np.concatenate((result10,result20))*100



datasets0=pd.read_csv('/Users/jiajiaxu/PycharmProjects/JsonToCsv/paybackperiod_savings/egalitarian_lgchemresu.csv')
X0=datasets0.values
d1=X0[:,6]
d2=X0[:,8]
X=[]
for j in range(len(d1)):
    if d1[j]>=0 and d2[j]>=0:
        X.append(X0[j,:])
    else:
        X.append([0, 0, 0, 0, 0, 0, 0, 0,0])
X=np.array(X)

r10= X[:, 3]
r20= X[:, 4]
r0=np.concatenate((r10,r20))*100
Y0=[] #positive results
for i in range(len(r10)):
    if r10[i]>=0 and r20[i]>=0:
        Y0.append(X[i, :])
Y0=np.array(Y0)

result10=Y0[:,3]
result20=Y0[:,4]
result1=np.concatenate((result10,result20))*100



datasets0=pd.read_csv('/Users/jiajiaxu/PycharmProjects/JsonToCsv/paybackperiod_savings/egalitarian_teslapowerwall2.csv')
X0=datasets0.values
d1=X0[:,6]
d2=X0[:,8]
X=[]
for j in range(len(d1)):
    if d1[j]>=0 and d2[j]>=0:
        X.append(X0[j,:])
    else:
        X.append([0, 0, 0, 0, 0, 0, 0, 0,0])
X=np.array(X)

r10= X[:, 3]
r20= X[:, 4]
r0=np.concatenate((r10,r20))*100
Y0=[] #positive results
for i in range(len(r10)):
    if r10[i]>=0 and r20[i]>=0:
        Y0.append(X[i, :])
Y0=np.array(Y0)

result10=Y0[:,3]
result20=Y0[:,4]
result2=np.concatenate((result10,result20))*100


datasets0=pd.read_csv('/Users/jiajiaxu/PycharmProjects/JsonToCsv/paybackperiod_savings/proportational_ampetusenergypod.csv')
X0=datasets0.values
d1=X0[:,6]
d2=X0[:,8]
X=[]
for j in range(len(d1)):
    if d1[j]>=0 and d2[j]>=0:
        X.append(X0[j,:])
    else:
        X.append([0, 0, 0, 0, 0, 0, 0, 0,0])
X=np.array(X)

r10= X[:, 3]
r20= X[:, 4]
r0=np.concatenate((r10,r20))*100
Y0=[] #positive results
for i in range(len(r10)):
    if r10[i]>=0 and r20[i]>=0:
        Y0.append(X[i, :])
Y0=np.array(Y0)

result10=Y0[:,3]
result20=Y0[:,4]
result3=np.concatenate((result10,result20))*100


datasets0=pd.read_csv('/Users/jiajiaxu/PycharmProjects/JsonToCsv/paybackperiod_savings/proportational_lgchemresu.csv')
X0=datasets0.values
d1=X0[:,6]
d2=X0[:,8]
X=[]
for j in range(len(d1)):
    if d1[j]>=0 and d2[j]>=0:
        X.append(X0[j,:])
    else:
        X.append([0, 0, 0, 0, 0, 0, 0, 0,0])
X=np.array(X)

r10= X[:, 3]
r20= X[:, 4]
r0=np.concatenate((r10,r20))*100
Y0=[] #positive results
for i in range(len(r10)):
    if r10[i]>=0 and r20[i]>=0:
        Y0.append(X[i, :])
Y0=np.array(Y0)

result10=Y0[:,3]
result20=Y0[:,4]
result4=np.concatenate((result10,result20))*100



datasets0=pd.read_csv('/Users/jiajiaxu/PycharmProjects/JsonToCsv/paybackperiod_savings/proportational_teslapowerwall2.csv')
X0=datasets0.values
d1=X0[:,6]
d2=X0[:,8]
X=[]
for j in range(len(d1)):
    if d1[j]>=0 and d2[j]>=0:
        X.append(X0[j,:])
    else:
        X.append([0, 0, 0, 0, 0, 0, 0, 0,0])
X=np.array(X)

r10= X[:, 3]
r20= X[:, 4]
r0=np.concatenate((r10,r20))*100
Y0=[] #positive results
for i in range(len(r10)):
    if r10[i]>=0 and r20[i]>=0:
        Y0.append(X[i, :])
Y0=np.array(Y0)
result10=Y0[:,3]
result20=Y0[:,4]
result5=np.concatenate((result10,result20))*100


datasets0=pd.read_csv('/Users/jiajiaxu/PycharmProjects/JsonToCsv/paybackperiod_savings/equal_ampetusenergypod.csv')
X0=datasets0.values
d1=X0[:,6]
d2=X0[:,8]
X=[]
for j in range(len(d1)):
    if d1[j]>=0 and d2[j]>=0:
        X.append(X0[j,:])
    else:
        X.append([0, 0, 0, 0, 0, 0, 0, 0,0])
X=np.array(X)

r10= X[:, 3]
r20= X[:, 4]
r0=np.concatenate((r10,r20))*100
Y0=[] #positive results
for i in range(len(r10)):
    if r10[i]>=0 and r20[i]>=0:
        Y0.append(X[i, :])
Y0=np.array(Y0)

result10=Y0[:,3]
result20=Y0[:,4]
result6=np.concatenate((result10,result20))*100



datasets0=pd.read_csv('/Users/jiajiaxu/PycharmProjects/JsonToCsv/paybackperiod_savings/equal_lgchemresu.csv')
X0=datasets0.values

d1=X0[:,6]
d2=X0[:,8]
X=[]
for j in range(len(d1)):
    if d1[j]>=0 and d2[j]>=0:
        X.append(X0[j,:])
    else:
        X.append([0, 0, 0, 0, 0, 0, 0, 0,0])
X=np.array(X)

r10= X[:, 3]
r20= X[:, 4]
r0=np.concatenate((r10,r20))*100
Y0=[] #positive results
for i in range(len(r10)):
    if r10[i]>=0 and r20[i]>=0:
        Y0.append(X[i, :])
Y0=np.array(Y0)

result10=Y0[:,3]
result20=Y0[:,4]
result7=np.concatenate((result10,result20))*100


datasets0=pd.read_csv('/Users/jiajiaxu/PycharmProjects/JsonToCsv/paybackperiod_savings/equal_teslapowerwall2.csv')
X0=datasets0.values

d1=X0[:,6]
d2=X0[:,8]
X=[]
for j in range(len(d1)):
    if d1[j]>=0 and d2[j]>=0:
        X.append(X0[j,:])
    else:
        X.append([0, 0, 0, 0, 0, 0, 0, 0,0])
X=np.array(X)

r10= X[:, 3]
r20= X[:, 4]
r0=np.concatenate((r10,r20))*100
Y0=[] #positive results
for i in range(len(r10)):
    if r10[i]>=0 and r20[i]>=0:
        Y0.append(X[i, :])
Y0=np.array(Y0)

result10=Y0[:,3]
result20=Y0[:,4]
result8=np.concatenate((result10,result20))*100




fig,ax=plt.subplots(3,3)


ax[0,0].hist(x=result0, bins='auto', color='#0504aa',
                            alpha=0.7, rwidth=0.85,density=True)
ax[0,0].set_title('egalitarian_ampetusenergypod_payback year saving(percentage)')
ax[0,0].set_ylabel('proportion')



ax[0,1].hist(x=result1, bins='auto', color='#0504aa',
                            alpha=0.7, rwidth=0.85,density=True)
ax[0,1].set_title('egalitarian_lgchemresu_payback year saving(percentage)')
ax[0,1].set_ylabel('proportion')




ax[0,2].hist(x=result2, bins='auto', color='#0504aa',
                            alpha=0.7, rwidth=0.85,density=True)
ax[0,2].set_title('egalitarian_teslapowerwall2_payback year saving(percentage)')
ax[0,2].set_ylabel('proportion')



ax[1,0].hist(x=result3, bins='auto', color='#0504aa',
                            alpha=0.7, rwidth=0.85,density=True)
ax[1,0].set_title('proportational_ampetusenergypod_payback year saving(percentage)')
ax[1,0].set_ylabel('proportion')


ax[1,1].hist(x=result4, bins='auto', color='#0504aa',
                            alpha=0.7, rwidth=0.85,density=True)
ax[1,1].set_title('proportationl_lgchemresu_payback year saving(percentage)')
ax[1,1].set_ylabel('proportion')



ax[1,2].hist(x=result5, bins='auto', color='#0504aa',
                            alpha=0.7, rwidth=0.85,density=True)
ax[1,2].set_title('proportational_teslapowerwall2_payback year saving(percentage)')
ax[1,2].set_ylabel('proportion')



ax[2,0].hist(x=result6, bins=7, color='#0504aa',
                            alpha=0.7, rwidth=0.85,density=True)
ax[2,0].set_title('equal_ampetusenergypod_payback year saving(percentage)')
ax[2,0].set_ylabel('proportion')


ax[2,1].hist(x=result7, bins=7, color='#0504aa',
                            alpha=0.7, rwidth=0.85,density=True)
ax[2,1].set_title('equal_lgchemresu_payback year saving(percentage)')
ax[2,1].set_ylabel('proportion')



ax[2,2].hist(x=result8 ,density=True, bins=7, color='#0504aa',
                            alpha=0.7, rwidth=0.85)
ax[2,2].set_title('equal_teslapowerwall2_payback year saving(percentage)')
ax[2,2].set_ylabel('proportion')






plt.show()

