#BEZ OTPORA

import numpy as np
import matplotlib.pyplot as plt

m=1.0 #kg - masa
k=100.0 #N/m - konstanta elasticnosti opruge
v0=0.0 #m/s - pocetna brzina
vreme=10.0 #s ukupno vreme
g=9.81 # m/s^2

dt=1e-3 # s - vremenski korak
y0 = -m*g/k
n=int(round(vreme/dt))

#pravimo nizove dimenzije n
t=np.zeros(n,float)
v=np.zeros(n,float)
y=np.zeros(n,float)

#postavljamo pocetne vrednosti kao prve u nizu
y[0]=0.0
v[0]=v0

for i in range(n-1):
    F=-k*y[i] - m*g # Rezultujuca sila
    a=F/m
    # Ojler-Kromer
    v[i+1]=v[i]+ a*dt
    y[i+1]= y[i] + v[i+1]*dt
    t[i+1]=t[i]+dt


print("maksimalna visina:",max(y))
print("minimalna visina:",min(y))
print()
print("maksimalna brzina:",max(v))
print("minimalna brzina:",min(v))

fig,axs = plt.subplots(2)
fig.set_figwidth(10)
fig.set_figheight(10)

axs[0].set_title("Zavisnost brzine od vremena")
axs[0].set(xlabel="t[s]",ylabel="v[m/s]")
axs[0].set_xticks(np.arange(0,10.5,0.5))
axs[0].plot(t,v,"b")
axs[0].axhline(y=max(v),color='k',linestyle='--')
axs[0].axhline(y=min(v),color='k',linestyle='--')
axs[0].grid()

axs[1].set_title("Zavisnost visine od vremena")
axs[1].set(xlabel="t[s]",ylabel="y[m]")
axs[1].set_xticks(np.arange(0,10.5,0.5))
axs[1].plot(t,y,"r")
axs[1].axhline(y=max(y),color='k',linestyle='--')
axs[1].axhline(y=min(y),color='k',linestyle='--')
axs[1].axhline(y=y0,color='k',linestyle='--')
axs[1].grid()

fig.tight_layout()
plt.show()
