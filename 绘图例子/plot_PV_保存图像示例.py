# % 一些可用数据：
# % (wiki) Tc = 31.03℃=304.18K, Pc=7.38Mpa = 72.83493708atm
# % (pdf) a=3.592atm dm^6 mol^-2,b=0.04267dm^3/mol,R=0.082054,T=298K
import sympy as sp
import numpy as np
from matplotlib import pyplot as plt
from FPI import fpi_abs, fpi_rel
from Newton import newton
import matplotlib
matplotlib.rcParams['font.family']='SimHei'


x, p = sp.symbols('x p')

R = 0.082054

Tc = 304.18
Pc = 72.83493708
Vc = 0.094

#(wiki)
b0=0.178
b1=-0.044
b2=-1.517
b3=0.039
c0=0.428
c1=-0.422
c2=-0.008
c3=0.687
f0=0.0490
f1=9.52*10**(-4)



v_data = np.linspace(0.05, 0.5, 300)
rho_data = Vc/v_data





T = 373.15 #100
tr=T/Tc
b = b0+b1/tr+b2/tr**2+b3/tr**3
c = c0+c1/tr+c2/tr**2+c3/tr**3
f = f0+f1/tr
p_data = R*T/v_data * (1 + b*rho_data + c*rho_data**2 + f*rho_data**5)
plt.plot(v_data, p_data, label=r'$T = 373.15K\ \ (100^\circ C)$')


T = 323.15 #50
tr=T/Tc
b = b0+b1/tr+b2/tr**2+b3/tr**3
c = c0+c1/tr+c2/tr**2+c3/tr**3
f = f0+f1/tr
p_data = R*T/v_data * (1 + b*rho_data + c*rho_data**2 + f*rho_data**5)
plt.plot(v_data, p_data, label=r'$T = 323.15K\ \ (50^\circ C)$')


T = 304.18 #31.03
tr=T/Tc
b = b0+b1/tr+b2/tr**2+b3/tr**3
c = c0+c1/tr+c2/tr**2+c3/tr**3
f = f0+f1/tr
p_data = R*T/v_data * (1 + b*rho_data + c*rho_data**2 + f*rho_data**5)
plt.plot(v_data, p_data, label=r'$T_c = 304.18K\ \ (31.03^\circ C)$')


T = 298 #24.85
tr=T/Tc
b = b0+b1/tr+b2/tr**2+b3/tr**3
c = c0+c1/tr+c2/tr**2+c3/tr**3
f = f0+f1/tr
p_data = R*T/v_data * (1 + b*rho_data + c*rho_data**2 + f*rho_data**5)
plt.plot(v_data, p_data, label=r'$T = 298K\ \ (24.85^\circ C)$')


T = 273.15 #0
tr=T/Tc
b = b0+b1/tr+b2/tr**2+b3/tr**3
c = c0+c1/tr+c2/tr**2+c3/tr**3
f = f0+f1/tr
p_data = R*T/v_data * (1 + b*rho_data + c*rho_data**2 + f*rho_data**5)
plt.plot(v_data, p_data, label=r'$T = 273.15K\ \ (0^\circ C)$')


T = 263.15 #-10
tr=T/Tc
b = b0+b1/tr+b2/tr**2+b3/tr**3
c = c0+c1/tr+c2/tr**2+c3/tr**3
f = f0+f1/tr
p_data = R*T/v_data * (1 + b*rho_data + c*rho_data**2 + f*rho_data**5)
plt.plot(v_data, p_data, label=r'$T = 263.15K\ \ (-10^\circ C)$')





plt.legend()
plt.xlabel(r'$V_m/(dm^3\ mol^{-1})$')
plt.ylabel(r'$P/(atm)$')
plt.axis([0, 0.5, 0, 150])
plt.savefig("Fig-7-PV-virial.png",dpi=600)#注意要放在show之前

plt.show()