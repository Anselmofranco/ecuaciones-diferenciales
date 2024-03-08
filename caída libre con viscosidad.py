#caída libre con viscosidad

import matplotlib.pyplot as plt
dt = 0.1
x=18 
v=10
k=3  
m=2
a=-9.8-(k/m)*v
t=0
while t<4: #// aquí podría ir cualquier evaluacion de condicion final.
    plt.figure(1)
    plt.plot(t,x,"ro")
    plt.plot(t, v, "go")
    
    Ec=0.5*m*v**2
    Epg=m*9.8*x    
    Em=Ec+Epg
    plt.figure(2)
    plt.plot(t,Epg,"bo")
    plt.plot(t,Ec,"go")
    plt.plot(t,Em,"ro")    
    
    print (t, x)
    x=x+v*dt #valor es igual al valor derivado*dt
    v = v+a*dt
    a = -9.8-(k/m)*v #si el movimiento es una caida libre o un tiro vertical, la aceleración no se modificará.
    t = t+dt
        

plt.figure(1)
plt.show()
plt.figure(2)
plt.show()