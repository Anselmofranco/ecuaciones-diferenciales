#crecimiento de tumores canceri­genos mediante la ley de Gompertz
# N=-a.N.log(b.N)

import matplotlib.pyplot as plt
import math as m
dt = 0.01
a=0.2
b=0.4
N=0.2
N_1=-a*N*m.log(b*N)
t=0
while t<20: 
    N=N+N_1*dt
    t = t+dt
    N_1=-a*N*m.log(b*N)
    plt.figure(1)
    plt.plot(N,N_1,"ro")
    plt.figure(2)
    plt.plot(t,N,"bx")

plt.figure(1)
plt.show()
plt.figure(2)
plt.show()

