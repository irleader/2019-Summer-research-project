import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import *

x=pd.read_csv('/Users/jiajiaxu/PycharmProjects/JsonToCsv/microgrid/2011-04-02-b6.csv',header=None)
x=x.values

time=x[:,0]
demand=x[:,1]

time=time[::-1] # reverse the order of time
#time=np.flipud(time)
demand=demand[::-1] # reverse order of demand

constant=time[0]

for i in range(len(time)):
    time[i]=time[i]-constant

result=np.zeros((len(time),2))
result[:,0]=time
result[:,1]=demand
result=pd.DataFrame(result)
result.to_csv('{0}extracted.csv'.format('2011-04-02-b6'),header=None)


#half hourly data
time_interval=30
no_of_data=48
time1=np.zeros(no_of_data)
demand1=np.zeros(no_of_data)
result1=np.zeros((no_of_data,2))
for i in np.arange(0,no_of_data):
    time1[i]=time[i*time_interval]
    demand1[i]=demand[i*time_interval]
result1[:,0]=time1


result1[:,1]=demand1
result1=pd.DataFrame(result1)
result1.to_csv('{0}extracted{1}.csv'.format('2011-04-02-b6','half_hourly'),header=None)