import sympy as sp
import numpy as np
from FPI import fpi_abs, fpi_rel
from Newton import newton
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='SimHei'


R = 0.082054
a = 3.592
b = 0.04267

v_data = np.linspace(0.05, 1, 500)


T = 273.15 #0
p_data = R*T/(v_data - b) - a/v_data**2
plt.plot(v_data, p_data, label=r'$T = 273.15K\ \ (0^\circ C)$')

plt.plot([0.0770232095980422, 0.303153756563387], [46.9589180011999]*2, color='purple', label='气-液相变等温线  '+r'$P=46.96\ atm$')
plt.plot([0, 0.0770232095980422], [46.9589180011999]*2, color='purple', linestyle=':')
plt.plot([0.303153756563387, 0.6], [46.9589180011999]*2, color='purple', linestyle=':')



plt.legend()
plt.xlabel(r'$V_m/(dm^3\ mol^{-1})$')
plt.ylabel(r'$P/(atm)$')
plt.axis([0, 0.55, 25, 65])
plt.savefig("Fig-9-Maxwell.png",dpi=600)#注意要放在show之前
plt.show()
