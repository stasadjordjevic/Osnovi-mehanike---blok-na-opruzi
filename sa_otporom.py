#SA OTPOROM
import numpy as np
import matplotlib.pyplot as plt
from math import *

m=1.0 #kg   - masa tela (bloka)
k=100.0 #N/m  - konstanta elasticnosti opruge
v0=0.0 #m/s   - pocetna brzina
vreme=15.0 #s   - ukupno vreme 
g=9.81 # m/s^2
D= 2.5 #m^-1 - koeficijent otpora

#pretpostavljamo da se pri ovoj brzini menja smer otpora
vt=0.2 #m/s - granicna brzina

kv=D*vt #s^-1 konstanta otpora 

dt=1e-4 #s - vremenski korak


n=int(round(vreme/dt))
t=np.zeros(n,float)
y=np.zeros(n,float)
v=np.zeros(n,float)

y0 = -m*g/k
print("ravnotezni polozaj",y0)
#pocetni uslovi
y[0]=0.0
v[0]=v0

#ojler-kromer
for i in range(n-1):
    # proveravamo v da bismo znali koju formulu da koristimo za silu otpora
    if(v[i]<vt):
        Fot = -kv*v[i]
    else:
        Fot = -D*v[i]*abs(v[i])
    T = -k*y[i] 
    F = T - m*g + Fot  # k*y[i]=T - sila zatezanja
    a = F/m
    # Ojler-Kromer
    v[i+1] = v[i] + a*dt
    y[i+1] = y[i] + v[i+1]*dt
    t[i+1] = t[i] + dt



fig,axs = plt.subplots(2)
fig.set_figwidth(10)
fig.set_figheight(10)


axs[0].set_title("Zavisnost brzine od vremena")
axs[0].set(xlabel="t[s]",ylabel="v[m/s]")
axs[0].set_xticks(np.arange(0,vreme+0.1,1))
axs[0].plot(t,v,"r")
axs[0].grid()

axs[1].set_title("Zavisnost visine od vremena")
axs[1].set(xlabel="t[s]",ylabel="y[m]")
axs[1].set_xticks(np.arange(0,vreme+0.1,1))
axs[1].plot(t,y,"b")
axs[1].grid()

fig.tight_layout()
plt.show()