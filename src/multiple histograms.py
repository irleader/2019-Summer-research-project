import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

datasets1=pd.read_csv('/Users/jiajiaxu/PycharmProjects/JsonToCsv/histogram_data/histograms for stable coalition battery 4.5kwh.csv')
datasets1=datasets1.values
datasets2=pd.read_csv('/Users/jiajiaxu/PycharmProjects/JsonToCsv/histogram_data/histograms for stable coalition_amp.csv')
datasets2=datasets2.values

equal1=datasets1[:,2].tolist()
prop1=datasets1[:,5].tolist()
nash1=datasets1[:,8].tolist()

equal2=datasets2[:,2].tolist()
prop2=datasets2[:,5].tolist()
nash2=datasets2[:,8].tolist()


plt.figure(1)
bins = np.linspace(0, 30, 30)
plt.hist(equal1,bins, alpha=0.5, label='equal1',color='red')
plt.hist(prop1,bins, alpha=0.5, label='prop1',color='yellow')
plt.hist(nash1,bins, alpha=0.5, label='nash1',color='blue')

plt.legend(loc='upper right')

plt.figure(2)
bins = np.linspace(0, 30, 30)
plt.hist(equal2,bins, alpha=0.5, label='equal1',color='red')
plt.hist(prop2,bins, alpha=0.5, label='prop1',color='yellow')
plt.hist(nash2,bins, alpha=0.5, label='nash1',color='blue')

plt.legend(loc='upper right')


plt.show()