import matplotlib.pyplot as plt
import numpy as np
import math

fig, ax = plt.subplots()
pi = 3.14
Rpm1 = 50*pi/30
Rpm2 = 100*pi/30
XL=[]
def EuclieanDistance(x2,y2,x1,y1):
    return math.sqrt((x2-x1)**2  + (y2-y1)**2)

def plot_curve(Xi,Yi,Thetai,UL,UR):
    t=0
    r=38
    L=317.5
    dt=0.1

    Xn=Xi
    Yn=Yi
    Thetan = 3.14 * Thetai / 180
    Cost = 0
# Xi, Yi,Thetai: Input point's coordinates
# Xs, Ys: Start point coordinates for plot function
# Xn, Yn, Thetan: End point coordintes

    while t<1.5:
        t = t + dt
        Xs = Xn
        Ys = Yn
        Xn += 0.5*r * (UL + UR) * math.cos(Thetan) * dt
        Yn += 0.5*r * (UL + UR) * math.sin(Thetan) * dt
        Thetan += (r / L) * (UR - UL) * dt
        Cost += EuclieanDistance(Xn,Yn,Xs,Ys)
        plt.plot([Xs, Xn], [Ys, Yn], color="blue")
    # Cost1 = EuclieanDistance(Xn,Yn,Xi,Yi)
    Thetan = 180 * (Thetan) / 3.14
    return Xn, Yn, Thetan, Cost
def plot_curve1(Xi,Yi,Thetai,UL,UR):
    t=0
    r=38
    L=317.5
    dt=1

    Xs=Xi
    Ys=Yi
    Thetan = 3.14 * Thetai / 180
    Cost = 0
    # Xi, Yi,Thetai: Input point's coordinates
    # Xs, Ys: Start point coordinates for plot function
    # Xn, Yn, Thetan: End point coordintes

    # while t<1:
    #     t = t + dt
    # Xs = Xn
    # Ys = Yn
    Thetan = (r / L) * (UR - UL) * dt
    Xn = 0.5*r * (UL + UR) * math.cos(Thetan) * dt
    Yn = 0.5*r * (UL + UR) * math.sin(Thetan) * dt

    Cost = EuclieanDistance(Xn,Yn,Xs,Ys)
    plt.plot([Xs, Xn], [Ys, Yn], color="blue")
# Cost1 = EuclieanDistance(Xn,Yn,Xi,Yi)
    Thetan = 180 * (Thetan) / 3.14
    return Xn, Yn, Thetan, Cost

# def plot_curve(X0,Y0,Theta0,UL,UR):
#     t=0
#     r=38
#     L=317.5
#     dt=0.1
#     X1=0
#     Y1=0
#     dtheta=0
#     Theta0=3.14*Theta0/180
#     Theta1=Theta0
#     while t<1:
#         t=t+dt
#         X0=X0+X1
#         Y0=Y0+Y1
#         dx=r*1/2*(UL+UR)*math.cos(Theta1)*dt
#         dy=r*1/2*(UL+UR)*math.sin(Theta1)*dt
#         dtheta=(r/L)*(UR-UL)*dt
#         X1=X1+dx
#         Y1=Y1+dy
#         Theta1=Theta1+dtheta
#         plt.quiver(X0, Y0, X1, Y1,units='xy' ,scale=1,color= 'r',width =10, headwidth = 1,headlength=0)
#         # plt.pause(0.01)
#         Xn=X0+X1
#         Yn=Y0+Y1
#         Thetan=180*(Theta1)/3.14
#         # plt.quiver(X0, Y0, Xn, Yn,units='xy' ,scale=1,color= 'r',width =0.2, headwidth = 1,headlength=0)
#
#     return Xn,Yn,Thetan

plt.grid()

ax.set_aspect('equal')

plt.xlim(-10000,10000)
plt.ylim(-10000,10000)

plt.title('How to plot a vector in matplotlib ?',fontsize=10)


actions=[[0,Rpm1],[Rpm1,0],[Rpm1,Rpm1],[0,Rpm2],[Rpm2,0],[Rpm2,Rpm2],[Rpm1,Rpm2],[Rpm2,Rpm1]]

# for action in actions:
#     X1= plot_curve(0,0,0, action[0],action[0])# (0,0,45) hypothetical start configuration
#     print("X1",X1)
#     for action in actions:
#         X2=plot_curve(X1[0],X1[1],X1[2], action[0],action[1])
#         print("x2",X2)
#         plt.pause(0.1)

X1= (0,0,0,0,0)# (0,0,45) hypothetical start configuration
print("X1",X1)
for action in actions:
    X2=plot_curve(X1[0],X1[1],X1[2], action[0],action[1])
    print("x2",X2)
    plt.scatter(X2[0],X2[1])
    # X2=plot_curve1(X1[0],X1[1],X1[2], action[0],action[1])
    # plt.scatter(X2[0],X2[1])
    # print("x21",X2)
    plt.pause(0.1)
plt.show()
plt.close()
    
