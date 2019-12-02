import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

datasets=pd.read_csv('/Users/jiajiaxu/PycharmProjects/JsonToCsv/results_bruny_raw_4kW_teslapowerwall2.csv')

X=datasets.values
length=X.shape[0]


cust1=X[:,0]
cust2=X[:,1]

#get rid of self coalition
Y=[]
for i in range(length):
    if cust1[i]!=cust2[i]:
        Y.append(X[i,:])

X=np.array(Y)
            
cust1=X[:,0]
cust2=X[:,1]

#C_1=X[:,2]
C=X[:,3]

#C1_1=X[:,4]
C1=X[:,5]
C1_base=X[:,6]

#C2_1=X[:,7]
C2=X[:,8]
C2_base=X[:,9]

#dissimilarity=X[:,10]

days=X[:,11]

PV1_peak=X[:,12]
PV1_cost=X[:,13]
PV2_peak=X[:,14]
PV2_cost=X[:,15]

B1_capacity=X[:,16]
B1_cost=X[:,17]
B2_capacity=X[:,18]
B2_cost=X[:,19]

pbp_s1=(B1_cost+PV1_cost)/(C1_base-C1)/(365.25/days[0])
pbp_s2=(B2_cost+PV2_cost)/(C2_base-C2)/(365.25/days[0])

cust1_pbp_s1=np.column_stack((cust1,pbp_s1))
cust2_pbp_s2=np.column_stack((cust2,pbp_s2))

#cost function

# #equal split
# p1=C/2
# p2=C/2

# # proportional split
# utility_1=C1*((C1+C2-C)/(C1+C2))
# utility_2=C2*((C1+C2-C)/(C1+C2))
# p1=C1-utility_1
# p2=C2-utility_2

#Egalitarian/Nash
utility_1= (C2 + C1 - C) / 2
utility_2= (C2 + C1 - C) / 2
p1=C1-utility_1
p2=C2-utility_2

pbp_d1= (B1_cost+PV1_cost) / (C1_base - p1) / (365.25 / days[0])
pbp_d2= (B2_cost+PV2_cost) / (C2_base - p2) / (365.25 / days[0])


pbp_saving_1=(pbp_s1-pbp_d1)/pbp_s1
pbp_saving_2=(pbp_s2-pbp_d2)/pbp_s2



result=np.column_stack((cust1,cust2,pbp_saving_1,pbp_saving_2,pbp_s1,pbp_d1,pbp_s2,pbp_d2))
#result=pd.DataFrame(result)
#result.to_csv('equal_lgchemresu.csv',header=['cust1','cust2','pbp_saving1','pbp_saving2','pbp_sa1','pbp_co1','pbp_sa2','pbp_co2'])



outcome=[]
for i in range(32):
    if i==4 or i==8 or i==9 or i==14:
        continue
    R=[]# combinations of households
    P=[]#pay back year
    # direct connection
    for j in range(len(cust1)):
            if cust1[j]==i:
                R.append(X[j,0:2])
                P.append(pbp_saving_1[j])
            if cust2[j]==i:
                R.append(X[j,0:2])
                P.append(pbp_saving_2[j])
    R=np.array(R)
    P=np.array(P)

    Z=np.column_stack((R,P))
    #change order of first two columns
    for k in range(Z.shape[0]):
        if Z[k,1]==i:
            Z[k,1]=Z[k,0]
            Z[k,0]=i
    outcome.append(Z)


lis=[]
for i in range(len(outcome)):
    l=outcome[i]
    l=l.tolist()
    l.sort(key=lambda l:l[2],reverse=True)
    for j in range(len(l)):
        lis.append(l[j][1])

for i in range(len(lis)):
    if lis[i]>=5 and lis[i]<=7:
        lis[i]=lis[i]-1
    if lis[i]>=10 and lis[i]<=13:
        lis[i]=lis[i]-3
    if lis[i]>=15:
        lis[i]=lis[i]-4
    
    
#np.savetxt("list.csv", lis, delimiter=",", fmt='%s')







#
# outcome=pd.DataFrame(outcome)
# outcome.to_csv('test.csv',header=None)








for i in range(32):
    R=[]# combinations of households
    P=[]#pay back year
    # direct connection
    for j in range(len(cust1)):
            if cust1[j]==i:
                R.append(X[j,0:2])
                P.append(pbp_d1[j])
            if cust2[j]==i:
                R.append(X[j,0:2])
                P.append(pbp_d2[j])
    # #standalone
    # R.append([i,i])
    # p=None
    # for e in range(len(cust2_pbp_s2)):
    #     if cust2_pbp_s2[e,0]==i:
    #         p=cust2_pbp_s2[e,1]
    # # add the missing direct connection pay back year for household 0
    # if i==0:
    #     p=cust1_pbp_s1[0,1]
    # P.append(p)
    R=np.array(R)
    P=np.array(P)
    Z=np.column_stack((R,P))
    #change order of first two columns
    for k in range(Z.shape[0]):
        if Z[k,1]==i:
            Z[k,1]=Z[k,0]
            Z[k,0]=i

    #change from numpy array to pandas dataframe
    Z=pd.DataFrame(Z)
    #write Z to csv file
    #Z.to_csv('customer_{0}_payback_period.csv'.format(str(i)),header=None)





    





