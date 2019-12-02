import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

datasetw=pd.read_csv\
    ('/Users/jiajiaxu/PycharmProjects/JsonToCsv/processed_optimal_solution_4.5kwh_winter.csv')
Xw=datasetw.values

datasets=pd.read_csv\
    ('/Users/jiajiaxu/PycharmProjects/JsonToCsv/processed_optimal_solution_4.5kwh_summer.csv')
Xs=datasets.values

cust1=Xw[:,0]
cust2=Xw[:,1]

Cw=Xw[:,3]
C1w=Xw[:,5]
C2w=Xw[:,8]

Cs=Xs[:,3]
C1s=Xs[:,5]
C2s=Xs[:,8]

#cost function for winter
#equal split
p1we=Cw/2
p2we=Cw/2
#proportional split
utility_1wp=C1w*((C1w+C2w-Cw)/(C1w+C2w))
utility_2wp=C2w*((C1w+C2w-Cw)/(C1w+C2w))
p1wp=C1w-utility_1wp
p2wp=C2w-utility_2wp
#Nash/Egalitarian
utility_1wn= (C2w + C1w - Cw) / 2
utility_2wn= (C2w + C1w - Cw) / 2
p1wn=C1w-utility_1wn
p2wn=C2w-utility_2wn

#cost function for summer
#equal split
p1se=Cs/2
p2se=Cs/2
#proportional split
utility_1sp=C1s*((C1s+C2s-Cs)/(C1s+C2s))
utility_2sp=C2s*((C1s+C2s-Cs)/(C1s+C2s))
p1sp=C1s-utility_1sp
p2sp=C2s-utility_2sp
#Nash/Egalitarian
utility_1sn= (C2s + C1s - Cs) / 2
utility_2sn= (C2s + C1s - Cs) / 2
p1sn=C1s-utility_1sn
p2sn=C2s-utility_2sn


#indvidual saving (absolute value)
#equal
is1e=C1w+C1s-p1we-p1se
is2e=C2w+C2s-p2we-p2se
#proportional
is1p=C1w+C1s-p1wp-p1sp
is2p=C2w+C2s-p2wp-p2sp
#Nash/Egalitarian
is1n=C1w+C1s-p1wn-p1sn
is2n=C2w+C2s-p2wn-p2sn

#combine household combination with individual saving
#equal
re=np.column_stack((cust1,cust2,is1e,is2e))
#re=re.tolist()
#proportional
rp=np.column_stack((cust1,cust2,is1p,is2p))
#Nash/Egalitarian
rn=np.column_stack((cust1,cust2,is1n,is2n))

#social saving (absolute value)
ss=C1s+C1w+C2s+C2w-Cs-Cw
rss=np.column_stack((cust1,cust2,ss))


# extract all possible house combinations 26*25 from 325
# equal
nre = []
for i in range(32):
    temp = []
    for j in range(len(re)):
        if re[j][0] == i:
            temp.append(re[j])
        if re[j][1] == i:
            temp.append(re[j])
    temp = np.array(temp)
    for k in range(len(temp)):
        if temp[k, 1] == i:
            temp[k][0], temp[k][1] = temp[k][1], temp[k][0]
            temp[k][2], temp[k][3] = temp[k][3], temp[k][2]
    if temp.size != 0:
        nre.append(temp)

#rank the house combinations
rise=[]
for i in range(len(nre)):
    le=nre[i]
    le=le.tolist()
    le.sort(key=lambda le:le[2],reverse=True)
    for j in range(len(le)):
        rise.append(le[j])

# get rid of negatoive combinations for equal split
nnre = []
for i in range(len(rise)):
    if rise[i][2] >= 0 and rise[i][3] >= 0:
        nnre.append(rise[i])

# proportional
# nrp=[]
# for i in range(len(cust1)):
#     if rp[i,2]>=0 and rp[i,3]>=0:
#         nrp.append(rp[i,:])
nrp = []
for i in range(32):
    temp = []
    for j in range(len(rp)):
        if rp[j][0] == i:
            temp.append(rp[j])
        if rp[j][1] == i:
            temp.append(rp[j])
    temp = np.array(temp)
    for k in range(len(temp)):
        if temp[k][1] == i:
            temp[k][0], temp[k][1] = temp[k][1], temp[k][0]
            temp[k][2], temp[k][3] = temp[k][3], temp[k][2]
    if temp.size != 0:
        nrp.append(temp)
# Nash/Egalitarian
# nrn=[]
# for i in range(len(cust1)):
#     if rn[i,2]>=0 and rn[i,3]>=0:
#         nrn.append(rn[i,:])
nrn = []
for i in range(32):
    temp = []
    for j in range(len(rn)):
        if rn[j][0] == i:
            temp.append(rn[j])
        if rn[j][1] == i:
            temp.append(rn[j])
    temp = np.array(temp)
    for k in range(len(temp)):
        if temp[k][1] == i:
            temp[k][0], temp[k][1] = temp[k][1], temp[k][0]
            temp[k][2], temp[k][3] = temp[k][3], temp[k][2]
    if temp.size != 0:
        nrn.append(temp)



#import the coalition
amp_pro_col=pd.read_csv('/Users/jiajiaxu/PycharmProjects/stableroommate/stable coalition pairs_4.5kwh_prop.csv')
amp_nash_col=pd.read_csv('/Users/jiajiaxu/PycharmProjects/stableroommate/stable coalition pairs_4.5kwh_nash.csv')

amp_pro_col=amp_pro_col.values[:,0]
amp_nash_col=amp_nash_col.values[:,0]

index=[1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]

amp_pro_pair=np.column_stack((amp_pro_col,index))
amp_nash_pair=np.column_stack((amp_nash_col,index))

# find corresponding total individual savings (nrn,nrp)
pro_his_is=[]
for i in range(len(nrp)):
    for j in range(len(nrp[0])):
        for k in range(len(amp_pro_pair)):
            if nrp[i][j][0]==amp_pro_pair[k][0] and nrp[i][j][1]==amp_pro_pair[k][1]:
                pro_his_is.append(nrp[i][j][3])


nash_his_is=[]
for i in range(len(nrn)):
    for j in range(len(nrn[0])):
        for k in range(len(amp_nash_pair)):
            if nrn[i][j][0]==amp_nash_pair[k][0] and nrn[i][j][1]==amp_nash_pair[k][1]:
                nash_his_is.append(nrn[i][j][3])
                
#social optimal saving(rss)
optimal_pair=[[1,13],[2,30],[3,17],[4,9],[5,16],[6,24],[7,21],[8,18],[10,12],[14,27],[15,22],[19,23],[20,31],[25,28],[26,29]]
optimal_hist_pair=optimal_pair*2

optimal_hist_saving=[]
for i in range(len(rss)):
    for j in range(len(optimal_pair)):
        if rss[i][0]==optimal_pair[j][0] and rss[i][1]==optimal_pair[j][1]:
            optimal_hist_saving.append(rss[i][2])
optimal_hist_saving_2=optimal_hist_saving*2

#equal total individual saving(nre)
equal_pair=[[1,14],[2,19],[3,23],[4,21],[5,22],[6,28],[7,30],[8,31],[9,25],[10,24],[12,29],[13,17],[14,1],
            [15,16],[16,15],[17,13],[18,20],[19,2],[20,18],[21,4],[22,5],[23,3],[24,10],
            [25,9],[28,6],[29,12],[30,7],[31,8]]

equal_hist_pair=equal_pair.copy()
equal_hist_pair.append([26])
equal_hist_pair.append([27])




equal_hist_pair=np.array(equal_hist_pair)

equal_hist_is=[]
for i in range(len(nre)):
    for j in range(len(nre[0])):
        for k in range(len(equal_pair)):
            if nre[i][j][0]==equal_pair[k][0] and nre[i][j][1]==equal_pair[k][1]:
                equal_hist_is.append(nre[i][j][2])
for i in range(2):
    equal_hist_is.append(0)




to_be_ploted=np.column_stack((equal_hist_pair,equal_hist_is,amp_pro_pair,pro_his_is,amp_nash_pair,nash_his_is,optimal_hist_pair,optimal_hist_saving_2))
pd.DataFrame(to_be_ploted).to_csv('histograms for stable coalition feedin 0.15.csv',
                                  header=('','equal','','','prop','','','nash','','','optimal'))



