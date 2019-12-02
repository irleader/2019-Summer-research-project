import numpy as np
import pandas as pd

datasets = pd.read_csv\
('/Users/jiajiaxu/PycharmProjects/JsonToCsv/results_bruny_raw_4kW_ampetusenergypod_summer.csv')

X = datasets.values
length = X.shape[0]

cust1 = X[:, 0]
cust2 = X[:, 1]

Y = []
for i in range(length):
    if cust1[i] != cust2[i]:
        Y.append(X[i, :])

X = np.array(Y)

cust1 = X[:, 0]
cust2 = X[:, 1]

# C_1=X[:,2]
C = X[:, 3]

# C1_1=X[:,4]
C1 = X[:, 5]
C1_base = X[:, 6]

# C2_1=X[:,7]
C2 = X[:, 8]
C2_base = X[:, 9]

# dissimilarity=X[:,10]

days = X[:, 11]

PV1_peak = X[:, 12]
PV1_cost = X[:, 13]
PV2_peak = X[:, 14]
PV2_cost = X[:, 15]

B1_capacity = X[:, 16]
B1_cost = X[:, 17]
B2_capacity = X[:, 18]
B2_cost = X[:, 19]

pbp_s1 = (B1_cost + PV1_cost) / (C1_base - C1) / (365.25 / days[0])
pbp_s2 = (B2_cost + PV2_cost) / (C2_base - C2) / (365.25 / days[0])

cust1_pbp_s1 = np.column_stack((cust1, pbp_s1))
cust2_pbp_s2 = np.column_stack((cust2, pbp_s2))

# cost function

# #equal split
# p1=C/2
# p2=C/2

# # proportional split
# utility_1=C1*((C1+C2-C)/(C1+C2))
# utility_2=C2*((C1+C2-C)/(C1+C2))
# p1=C1-utility_1
# p2=C2-utility_2

# Egalitarian/Nash
utility_1 = (C2 + C1 - C) / 2
utility_2 = (C2 + C1 - C) / 2
p1 = C1 - utility_1
p2 = C2 - utility_2

pbp_d1 = (B1_cost + PV1_cost) / (C1_base - p1) / (365.25 / days[0])
pbp_d2 = (B2_cost + PV2_cost) / (C2_base - p2) / (365.25 / days[0])

pbp_saving_1 = (pbp_s1 - pbp_d1) / pbp_s1
pbp_saving_2 = (pbp_s2 - pbp_d2) / pbp_s2

social_saving=1-C/(C1+C2)

individual_saving_1=(C1-p1)/C1
individual_saving_2=(C2-p2)/C2

result=np.column_stack((cust1,cust2,social_saving,individual_saving_1,individual_saving_2,pbp_saving_1,pbp_saving_2))




# outcome=[]
# for i in range(32):
#     S = []
#     for j in range(len(cust1)):
#             if cust1[j]==i:
#                 S.append(social_saving[j])
#             if cust2[j]==i:
#                 S.append(social_saving[j])
#     outcome=np.concatenate((outcome,S))

ss_table = [[None]*32 for _ in range(32)]
for j in range(len(cust1)):
    for i in range(32):
        if cust1[j] == i:
            ss_table[i][int(cust2[j])]=social_saving[j]
        if cust2[j] == i:
            ss_table[i][int(cust1[j])] = social_saving[j]
ss_table=pd.DataFrame(ss_table)
ss_table.to_csv('offline_social_saving_table.csv')

is_table=[[None]*32 for _ in range(32)]
for j in range(len(cust1)):
    for i in range(32):
        if cust1[j]==i:
            is_table[i][int(cust2[j])]=individual_saving_1[j]
            is_table[int(cust2[j])][i]=individual_saving_2[j]
is_table=pd.DataFrame(is_table)
is_table.to_csv('offline_individual_saving_table.csv')

ps_table= [[None]*32 for _ in range(32)]
for j in range(len(cust1)):
    for i in range(32):
        if cust1[j]==i:
            ps_table[i][int(cust2[j])]=pbp_saving_1[j]
            ps_table[int(cust2[j])][i]=pbp_saving_2[j]
ps_table=pd.DataFrame(ps_table)
ps_table.to_csv('offline_periodbackperiod_saving_table.csv')


