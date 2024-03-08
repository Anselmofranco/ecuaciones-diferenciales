#Modelado de dos cargas puntuales aceleradas debido repulsión electrostática.
# Grafico de posición, trabajo electrostático y energía cinética.

import matplotlib.pyplot as plt
dt = 0.01
k=9e9
q=2*1.6e-19
m=9.11e-31
x=40
v=-1
F=q*q*k/(x**2)
a=F/m
t=0

 

while t<10: 
    plt.figure(1)
    plt.plot(t,x,"ro")
    plt.figure(2)
    plt.plot(t,0.5*m*v**2,"bo")
    plt.plot(t,F*x,"go")
    plt.plot(t,F*x+0.5*m*v**2,"ro")
    x=x+v*dt
    v=v+a*dt
    F=q*q*k/(x**2)
    a=F/m
    t = t+dt

 

plt.figure(1)
plt.show()
plt.figure(2)
plt.show()