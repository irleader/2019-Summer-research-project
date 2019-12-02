import numpy as np
import pandas as pd

datasetw=pd.read_csv\
    ('/Users/jiajiaxu/PycharmProjects/JsonToCsv/unsolvable/processed_results_eval_winter_feedin_0.08_lg.csv')
Xw=datasetw.values

datasets=pd.read_csv\
    ('/Users/jiajiaxu/PycharmProjects/JsonToCsv/unsolvable/processed_results_eval_summer_feedin_0.08_lg.csv')
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

# nss=[]
# for i in range(32):
#     temp=[]
#     for j in range(len(rss)):
#         if rss[j][0]==i:
#             temp.append(rss[j])
#         if rss[j][1]==i:
#             temp.append(rss[j])
#     temp=np.array(temp)
#     for k in range(len(temp)):
#         if temp[k,1]==i:
#             temp[k][0],temp[k][1] = temp[k][1], temp[k][0]
#     if temp.size!=0:
#         nss.append(temp)


#combine household combination with individual saving
#equal
re=np.column_stack((cust1,cust2,is1e,is2e))
#re=re.tolist()
#proportional
rp=np.column_stack((cust1,cust2,is1p,is2p))
#Nash/Egalitarian
rn=np.column_stack((cust1,cust2,is1n,is2n))



# extract all possible house combinations 26*25 from 325
#equal
nre=[]
for i in range(32):
    temp=[]
    for j in range(len(re)):
        if re[j][0]==i:
            temp.append(re[j])
        if re[j][1]==i:
            temp.append(re[j])
    temp=np.array(temp)
    for k in range(len(temp)):
        if temp[k,1]==i:
            temp[k][0],temp[k][1] = temp[k][1], temp[k][0]
            temp[k][2],temp[k][3] = temp[k][3], temp[k][2]
    if temp.size!=0:
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
                    

#proportional
# nrp=[]
# for i in range(len(cust1)):
#     if rp[i,2]>=0 and rp[i,3]>=0:
#         nrp.append(rp[i,:])
nrp=[]
for i in range(32):
    temp=[]
    for j in range(len(rp)):
        if rp[j][0]==i:
            temp.append(rp[j])
        if rp[j][1]==i:
            temp.append(rp[j])
    temp=np.array(temp)
    for k in range(len(temp)):
        if temp[k][1]==i:
            temp[k][0],temp[k][1]=temp[k][1],temp[k][0]
            temp[k][2],temp[k][3] = temp[k][3], temp[k][2]
    if temp.size!=0:
         nrp.append(temp)
#Nash/Egalitarian
# nrn=[]
# for i in range(len(cust1)):
#     if rn[i,2]>=0 and rn[i,3]>=0:
#         nrn.append(rn[i,:])
nrn=[]
for i in range(32):
    temp=[]
    for j in range(len(rn)):
        if rn[j][0]==i:
            temp.append(rn[j])
        if rn[j][1]==i:
            temp.append(rn[j])
    temp=np.array(temp)
    for k in range(len(temp)):
        if temp[k][1]==i:
            temp[k][0],temp[k][1]=temp[k][1],temp[k][0]
            temp[k][2],temp[k][3] = temp[k][3], temp[k][2]
    if temp.size!=0:
         nrn.append(temp)


# sort houses in rank to be processed by stable roommate algorithm
#equal
lise=[]
for i in range(len(nre)):
    le=nre[i]
    le=le.tolist()
    le.sort(key=lambda le:le[2],reverse=True)
    for j in range(len(le)):
        lise.append(le[j][1])

#proportional
lisp=[]
for i in range(len(nrp)):
    lp=nrp[i]
    lp=lp.tolist()
    lp.sort(key=lambda lp:lp[2],reverse=True)
    for j in range(len(lp)):
        lisp.append(lp[j][1])
#Nash/Egalitarian
lisn=[]
for i in range(len(nrn)):
    ln=nrn[i]
    ln=ln.tolist()
    ln.sort(key=lambda ln:ln[2],reverse=True)
    for j in range(len(ln)):
        lisn.append(ln[j][1])

# cheat to have certain format
#equal
for i in range(len(lise)):
    if lise[i]>=12:
        lise[i]=lise[i]-1
np.savetxt("equal_list.csv", lise, delimiter=",", fmt='%s')

#proportional
for i in range(len(lisp)):
    if lisp[i]>=12:
        lisp[i]=lisp[i]-1

np.savetxt("proportional_list.csv", lisp, delimiter=",", fmt='%s')

# lisp=np.array(lisp)
# lisp=lisp.reshape((29,30))
# lisp=np.transpose(lisp)
#Nash/Egalitarian
for i in range(len(lisn)):
    if lisn[i]>=12:
        lisn[i]=lisn[i]-1
np.savetxt("nash_list.csv", lisn, delimiter=",", fmt='%s')


#social saving (absolute value)
ss=C1s+C1w+C2s+C2w-Cs-Cw
rss=np.column_stack((cust1,cust2,ss))
str_cust1=list(map(str,cust1))
str_cust2=list(map(str,cust2))
possible_tables=list(zip(str_cust1,str_cust2))
nss=list(zip(possible_tables,ss))
#np.savetxt("social_saving.csv", ss, delimiter=",", fmt='%s')

nnre=np.array(nre).reshape((-1,4))
nnrn=np.array(nrn).reshape((-1,4))
nnrp=np.array(nrp).reshape((-1,4))
rss=rss.tolist()*2
nrss=np.array(rss)
result=np.column_stack((nnre,nnrn,nnrp,nrss))
    
np.savetxt('equal_full_individual_saving_4.5kwh.csv',nnre,delimiter=",", fmt='%s')
np.savetxt('prop_full_individual_saving_4.5kwh.csv',nnrp,delimiter=",", fmt='%s')
np.savetxt('nash_full_individual_saving_4.5kwh.csv',nnrn,delimiter=",", fmt='%s')

np.savetxt('full_individual_saving_time_feedin0.08_lg.csv',result,delimiter=",", fmt='%s')








