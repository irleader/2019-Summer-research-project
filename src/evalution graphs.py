import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset_amp=pd.read_csv(
    '/Users/jiajiaxu/PycharmProjects/JsonToCsv/histograms for stable coalition_amp.csv'
)
dataset_amp=dataset_amp.values
dataset_telsa=pd.read_csv(
    '/Users/jiajiaxu/PycharmProjects/JsonToCsv/histograms for stable coalition_telsa.csv'
)
dataset_telsa=dataset_telsa.values

equal_amp=dataset_amp[:,2]
prop_amp=dataset_amp[:,5]
nash_amp=dataset_amp[:,8]

equal_telsa=dataset_telsa[:,2]
prop_telsa=dataset_telsa[:,5]
nash_telsa=dataset_telsa[:,8]

plt.figure(1)
plt.hist([equal_amp, prop_amp,nash_amp], label=['equal_amp', 'prop_amp','nash_amp'])
plt.legend(loc='upper right')
plt.autoscale(tight=True)

plt.figure(2)
plt.hist([equal_telsa, prop_telsa,nash_telsa], label=['equal_telsa', 'prop_telsa','nash_telsa'])
plt.legend(loc='upper right')
plt.autoscale(tight=True)




# total_utiltiy
amp_equal_utility=346.91
amp_prop_utiltiy=405.57
amp_nash_utility=536.19
amp_optimal_utility=558.02

telsa_equal_utility=344.25
telsa_prop_utiltiy=366.89
telsa_nash_utility=514.77
telsa_optimal_utility=547.51

plt.figure(3)
plt.bar(x=0.35,height=[amp_equal_utility,amp_prop_utiltiy,amp_nash_utility,amp_optimal_utility],label=['amp_equal_utility','amp_prop_utiltiy','amp_nash_utility','amp_optimal_utility'])

plt.show()