import numpy as np
import pandas as pd

datasets=pd.read_csv('/Users/jiajiaxu/PycharmProjects/JsonToCsv/online_savings.csv')
X=datasets.values

cust1=X[:,0]
cust2=X[:,1]
ss=X[:,2]
ise1=X[:,3]
ise2=X[:,4]
isp1=X[:,5]
isp2=X[:,6]
iseg1=X[:,7]
iseg2=X[:,8]
pse1=X[:,9]
pse2=X[:,10]
psp1=X[:,11]
psp2=X[:,12]
pseg1=X[:,13]
pseg2=X[:,14]


ss_table=[[None]*32 for _ in range(32)]
for j in range(len(ss)):
    for i in range(32):
        if cust1[j]==i:
            ss_table[int(cust1[j])][int(cust2[j])]=ss[j]
            ss_table[int(cust2[j])][int(cust1[j])]=ss[j]
ss_table=pd.DataFrame(ss_table)
ss_table.to_csv('online_social_saving_table.csv')


ise_table=[[None]*32 for _ in range(32)]
for j in range(len(ise1)):
    for i in range(32):
        if cust1[j]==i:
            ise_table[int(cust1[j])][int(cust2[j])]=ise1[j]
            ise_table[int(cust2[j])][int(cust1[j])]=ise2[j]
ise_table=pd.DataFrame(ise_table)
ise_table.to_csv('online_individual_saving_equal_table.csv')


isp_table=[[None]*32 for _ in range(32)]
for j in range(len(isp1)):
    for i in range(32):
        if cust1[j]==i:
            isp_table[int(cust1[j])][int(cust2[j])]=isp1[j]
            isp_table[int(cust2[j])][int(cust1[j])]=isp2[j]
isp_table=pd.DataFrame(isp_table)
isp_table.to_csv('online_individual_saving_proportional_table.csv')


iseg_table=[[None]*32 for _ in range(32)]
for j in range(len(iseg1)):
    for i in range(32):
        if cust1[j]==i:
            iseg_table[int(cust1[j])][int(cust2[j])]=iseg1[j]
            iseg_table[int(cust2[j])][int(cust1[j])]=iseg2[j]
iseg_table=pd.DataFrame(iseg_table)
iseg_table.to_csv('online_individual_saving_egalitarian_table.csv')


pse_table=[[None]*32 for _ in range(32)]
for j in range(len(pse1)):
    for i in range(32):
        if cust1[j]==i:
            pse_table[int(cust1[j])][int(cust2[j])]=pse1[j]
            pse_table[int(cust2[j])][int(cust1[j])]=pse2[j]
pse_table=pd.DataFrame(pse_table)
pse_table.to_csv('online_paybackperiod_saving_equal_table.csv')

psp_table=[[None]*32 for _ in range(32)]
for j in range(len(psp1)):
    for i in range(32):
        if cust1[j]==i:
            psp_table[int(cust1[j])][int(cust2[j])]=psp1[j]
            psp_table[int(cust2[j])][int(cust1[j])]=psp2[j]
psp_table=pd.DataFrame(psp_table)
psp_table.to_csv('online_paybackperiod_saving_proportional_table.csv')


pseg_table=[[None]*32 for _ in range(32)]
for j in range(len(pseg1)):
    for i in range(32):
        if cust1[j]==i:
            pseg_table[int(cust1[j])][int(cust2[j])]=pseg1[j]
            pseg_table[int(cust2[j])][int(cust1[j])]=pseg2[j]
pseg_table=pd.DataFrame(pseg_table)
pseg_table.to_csv('online_paybackperiod_saving_egalitarian_table.csv')