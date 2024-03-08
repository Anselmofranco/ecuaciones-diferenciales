# Análisis de la ecuación logística usada para el estudio de poblaciones.
# espacio de fases y resolución para r=10 y k=300.

import matplotlib.pyplot as plt
dt = 0.01
k=300
r=10
N=500
N_1=r*N*(1-(N/k))
t=0
while t<3: 
    N=N+N_1*dt
    t = t+dt
    N_1=r*N*(1-(N/k))
    plt.figure(1)
    plt.plot(N,N_1,"ro")
    plt.figure(2)
    plt.plot(t,N,"bx")

plt.figure(1)
plt.show()
plt.figure(2)
plt.show()
