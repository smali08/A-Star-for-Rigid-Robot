import matplotlib.pyplot as plt
import numpy as np
import math

fig, ax = plt.subplots()
XL=[]
def plot_curve(X0,Y0,Theta0,UL,UR):
    t=0
    r=0.1
    L=1
    dt=0.1
    X1=0
    Y1=0
    dtheta=0
    Theta0=3.14*Theta0/180
    Theta1=Theta0
    while t<1:
        t=t+dt
        X0=X0+X1
        Y0=Y0+Y1
        dx=r*1/2*(UL+UR)*math.cos(Theta1)*dt
        dy=r*1/2*(UL+UR)*math.sin(Theta1)*dt
        dtheta=(r/L)*(UR-UL)*dt
        X1=X1+dx
        Y1=Y1+dy
        Theta1=Theta1+0.5*dtheta
        plt.quiver(X0, Y0, X1, Y1,units='xy' ,scale=1,color= 'r',width =0.2, headwidth = 1,headlength=0)
        # plt.pause(0.01)
        Xn=X0+X1
        Yn=Y0+Y1
        Thetan=180*(Theta1)/3.14
        # plt.quiver(X0, Y0, Xn, Yn,units='xy' ,scale=1,color= 'r',width =0.2, headwidth = 1,headlength=0)

    return Xn,Yn,Thetan

plt.grid()

ax.set_aspect('equal')

plt.xlim(-10,10)
plt.ylim(-10,10)

plt.title('How to plot a vector in matplotlib ?',fontsize=10)


actions=[[5,5],[5,0],[0,5],[5,10],[10,5],[10,0],[0,10],[10,10]]
        
for action in actions:
    X1= plot_curve(0,0,0, action[0],action[0])# (0,0,45) hypothetical start configuration
    print("X1",X1)
    for action in actions:
        X2=plot_curve(X1[0],X1[1],X1[2], action[0],action[1])
        print("x2",X2)
        plt.pause(0.1)


plt.show()
plt.close()
    
