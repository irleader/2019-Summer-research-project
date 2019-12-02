import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x=pd.read_csv("/Users/jiajiaxu/PycharmProjects/JsonToCsv/optimal_solution.csv")

x=x.values


s=0 #start hour
d=24 #end hour
ai=x[s:d,0]
rij=x[s:d,4]
raij=x[s:d,5]
rbij=x[s:d,6]
rgij=x[s:d,7]
bik=x[s:d,8]
daik=x[s:d,9]
dgik=x[s:d,10]
gi_minus =x[s:d,1]
gi_plus =x[s:d,2]
gai=x[s:d,3]
gbi=x[s:d,11]

a1=x[s:d,12]
a2=x[s:d,13]
r1j=x[s:d,14]
r2j=x[s:d,15]

t=np.arange(0,d-s)

fig1,ax1=plt.subplots(1,1,sharex=True,sharey=True)
ax1.plot(t,ai,label='total demand')
ax1.plot(t,a1,label='house1 demand')
ax1.plot(t,a2,label='hosue2 demand')
ax1.set_title('House demand')
ax1.set_xlabel('time')
ax1.set_ylabel('power(kW)')
plt.legend()
plt.tight_layout()

fig2,ax2=plt.subplots(1,1,sharex=True,sharey=True)
ax2.plot(t,rij,label='total generation')
ax2.plot(t,raij,label='PV to demand')
ax2.plot(t,rbij,label='PV to battery')
ax2.plot(t,rgij,label='PV to grid')
ax2.set_title('PV Generation')
ax2.set_xlabel('time')
ax2.set_ylabel('power(kW)')
plt.legend()
plt.tight_layout()


fig3,ax3=plt.subplots(1,1,sharex=True,sharey=True)
ax3.plot(t,rbij,label='PV to battery')
ax3.plot(t,gbi,label='Grid to battery')
ax3.plot(t,daik,label='battery to demand')
ax3.plot(t,dgik,label='battery to grid')
ax3.set_title('Battery')
ax3.set_xlabel('time')
ax3.set_ylabel('power(kW)')
plt.legend()
plt.tight_layout()

fig4,ax4=plt.subplots(1,1,sharex=True,sharey=True)
ax4.plot(t,gi_plus,label='Grid output')
ax4.plot(t,gi_minus,label='Sell to Grid')
ax4.set_title('Grid')
ax4.set_xlabel('time')
ax4.set_ylabel('power(kW)')
plt.legend()
plt.tight_layout()

plt.show()