#Sistema masa resorte. Posición, velocidad y energías.

import matplotlib.pyplot as plt
dt = 0.001
x=1 # los valores de xinicial, de v inicial, y de a inicial los pondrá usted, de acuerdo al caso a simular.
v=0
k=20  
m=2
a=-(k/m)*x
t=0
while t<3: #// aquí podría ir cualquier evaluacion de condicion final.
    plt.figure(1)
    plt.plot(t,x,"ro")
    plt.plot(t, v, "go")
    
    Ec=0.5*m*v**2
    Epk=0.5*k*x**2    
    Em=Ec+Epk
    plt.figure(2)
    plt.plot(t,Epk,"bo")
    plt.plot(t,Ec,"go")
    plt.plot(t,Em,"ro")    
    
   # print (t, x)
    v = v+a*dt
    x=x+v*dt #valor es igual al valor derivado*dt
    a = -(k/m)*x #si el movimiento es una caida libre o un tiro vertical, la aceleración no se modificará.
    t = t+dt
        

plt.figure(1)
plt.show()
plt.figure(2)
plt.show()
