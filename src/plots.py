import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x=pd.read_csv("/Users/jiajiaxu/PycharmProjects/JsonToCsv/x.csv",header=None)
x1=pd.read_csv("/Users/jiajiaxu/PycharmProjects/JsonToCsv/x1.csv",header=None)
x2=pd.read_csv("/Users/jiajiaxu/PycharmProjects/JsonToCsv/x2.csv",header=None)
x=x.values
x1=x1.values
x2=x2.values

length_of_hours=720
x=x.reshape(length_of_hours,12)
x1=x1.reshape(length_of_hours,12)
x2=x2.reshape(length_of_hours,12)


s=0 #start hour
d=168 #end hour
ai=x[s:d,0]
rij=x[s:d,1]
raij=x[s:d,2]
rbij=x[s:d,3]
rgij=x[s:d,4]
bik=x[s:d,5]
daik=x[s:d,6]
dgik=x[s:d,7]
gi_minus =x[s:d,8]
gi_plus =x[s:d,9]
gai=x[s:d,10]
gbi=x[s:d,11]

a1=x1[s:d,0]
r1j=x1[s:d,1]
ra1j=x1[s:d,2]
rb1j=x1[s:d,3]
rg1j=x1[s:d,4]
b1k=x1[s:d,5]
da1k=x1[s:d,6]
dg1k=x1[s:d,7]
g1_minus =x1[s:d,8]
g1_plus =x1[s:d,9]
ga1=x1[s:d,10]
gb1=x1[s:d,11]

a2=x2[s:d,0]
r2j=x2[s:d,1]
ra2j=x2[s:d,2]
rb2j=x2[s:d,3]
rg2j=x2[s:d,4]
b2k=x2[s:d,5]
da2k=x2[s:d,6]
dg2k=x2[s:d,7]
g2_minus =x2[s:d,8]
g2_plus =x2[s:d,9]
ga2=x2[s:d,10]
gb2=x2[s:d,11]

t=np.arange(0,d-s)


fig1,ax1=plt.subplots(3,1,sharex=True,sharey=True)
ax1[0].plot(t,ai,label='total')
ax1[0].set_title('Total Demand')
ax1[0].set_xlabel('time')
ax1[0].set_ylabel('power(kW)')

ax1[1].plot(t,a1)
ax1[1].set_title('House1 Demand')
ax1[1].set_xlabel('time')
ax1[1].set_ylabel('power(kW)')

ax1[2].plot(t,a2)
ax1[2].set_title('House2 Demand')
ax1[2].set_xlabel('time')
ax1[2].set_ylabel('power(kW)')
plt.tight_layout()

fig2,ax2=plt.subplots(3,1,sharex=True,sharey=True)
ax2[0].plot(t,rij,label='total')
ax2[0].set_title('Total PV Generation')
ax2[0].set_xlabel('time')
ax2[0].set_ylabel('power(kW)')

ax2[1].plot(t,r1j)
ax2[1].set_title('House1 PV Generation')
ax2[1].set_xlabel('time')
ax2[1].set_ylabel('power(kW)')

ax2[2].plot(t,r2j)
ax2[2].set_title('House2 PV Generation')
ax2[2].set_xlabel('time')
ax2[2].set_ylabel('power(kW)')
plt.tight_layout()


fig3,ax3=plt.subplots(3,1,sharex=True,sharey=True)
ax3[0].plot(t,bik,label='total')
ax3[0].set_title('Total Battery Energy')
ax3[0].set_xlabel('time')
ax3[0].set_ylabel('Energy(kJ)')

ax3[1].plot(t,b1k)
ax3[1].set_title('House1 Battery Energy')
ax3[1].set_xlabel('time')
ax3[1].set_ylabel('energy(kJ)')

ax3[2].plot(t,b2k)
ax3[2].set_title('House2 Battery Energy')
ax3[2].set_xlabel('time')
ax3[2].set_ylabel('energy(kJ)')
plt.tight_layout()

fig4,ax4=plt.subplots(3,1,sharex=True,sharey=True)
ax4[0].plot(t,gai,label='total')
ax4[0].set_title('Total Grid to Demand')
ax4[0].set_xlabel('time')
ax4[0].set_ylabel('Power(kW)')

ax4[1].plot(t,ga1)
ax4[1].set_title('Grid to House1 demand')
ax4[1].set_xlabel('time')
ax4[1].set_ylabel('power(kW)')

ax4[2].plot(t,ga2)
ax4[2].set_title('Grid to House2 demand')
ax4[2].set_xlabel('time')
ax4[2].set_ylabel('power(kW)')
plt.tight_layout()

fig5,ax5=plt.subplots(3,1,sharex=True,sharey=True)
ax5[0].plot(t,gbi,label='total')
ax5[0].set_title('Total Grid to Battery')
ax5[0].set_xlabel('time')
ax5[0].set_ylabel('Power(kW)')

ax5[1].plot(t,gb1)
ax5[1].set_title('Grid to House1 battery')
ax5[1].set_xlabel('time')
ax5[1].set_ylabel('power(kW)')

ax5[2].plot(t,gb2)
ax5[2].set_title('Grid to House2 battery')
ax5[2].set_xlabel('time')
ax5[2].set_ylabel('power(kW)')
plt.tight_layout()


fig6,ax6=plt.subplots(3,1,sharex=True,sharey=True)
ax6[0].plot(t,daik,label='total')
ax6[0].set_title('Total Battery to Demand')
ax6[0].set_xlabel('time')
ax6[0].set_ylabel('Power(kW)')

ax6[1].plot(t,da1k)
ax6[1].set_title('Battery to House1 demand')
ax6[1].set_xlabel('time')
ax6[1].set_ylabel('power(kW)')

ax6[2].plot(t,da2k)
ax6[2].set_title('Battery to House2 demand')
ax6[2].set_xlabel('time')
ax6[2].set_ylabel('power(kW)')
plt.tight_layout()


fig7,ax7=plt.subplots(3,1,sharex=True,sharey=True)
ax7[0].plot(t,dgik,label='total')
ax7[0].set_title('Total Battery to Grid')
ax7[0].set_xlabel('time')
ax7[0].set_ylabel('Power(kW)')

ax7[1].plot(t,dg1k)
ax7[1].set_title('House1 Battery to grid ')
ax7[1].set_xlabel('time')
ax7[1].set_ylabel('power(kW)')

ax7[2].plot(t,dg2k)
ax7[2].set_title('House2 Battery to grid')
ax7[2].set_xlabel('time')
ax7[2].set_ylabel('power(kW)')
plt.tight_layout()



fig8,ax8=plt.subplots(3,1,sharex=True,sharey=True)
ax8[0].plot(t,raij,label='total')
ax8[0].set_title('Total PV to Demand')
ax8[0].set_xlabel('time')
ax8[0].set_ylabel('Power(kW)')

ax8[1].plot(t,ra1j)
ax8[1].set_title('House1 PV to demand')
ax8[1].set_xlabel('time')
ax8[1].set_ylabel('power(kW)')

ax8[2].plot(t,ra2j)
ax8[2].set_title('House2 PV to demand')
ax8[2].set_xlabel('time')
ax8[2].set_ylabel('power(kW)')
plt.tight_layout()



fig9,ax9=plt.subplots(3,1,sharex=True,sharey=True)
ax9[0].plot(t,rbij,label='total')
ax9[0].set_title('Total PV to Battery')
ax9[0].set_xlabel('time')
ax9[0].set_ylabel('Power(kW)')

ax9[1].plot(t,rb1j)
ax9[1].set_title('House1 PV to battery')
ax9[1].set_xlabel('time')
ax9[1].set_ylabel('power(kW)')

ax9[2].plot(t,rb2j)
ax9[2].set_title('House2 PV to battery')
ax9[2].set_xlabel('time')
ax9[2].set_ylabel('power(kW)')
plt.tight_layout()



fig10,ax10=plt.subplots(3,1,sharex=True,sharey=True)
ax10[0].plot(t,rgij,label='total')
ax10[0].set_title('Total PV to Grid')
ax10[0].set_xlabel('time')
ax10[0].set_ylabel('Power(kW)')

ax10[1].plot(t,rg1j)
ax10[1].set_title('House1 PV to grid')
ax10[1].set_xlabel('time')
ax10[1].set_ylabel('power(kW)')

ax10[2].plot(t,rg2j)
ax10[2].set_title('House2 PV to grid')
ax10[2].set_xlabel('time')
ax10[2].set_ylabel('power(kW)')
plt.tight_layout()

plt.show()

