#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import copy
import math
import time
import numpy as np
import math
import rospy
from geometry_msgs.msg import Point, Twist, PoseStamped
import time

#Creating ROS Node
rospy.init_node('turtlebot_project', anonymous=True)  

#Defining Publisher
cmd_vel_pub_ = rospy.Publisher('/cmd_vel', Twist, queue_size = 10)

# Function to move robot in Gazebo by publishing velocity
def move_robot(pub, dvx, dvy, dw):  
     r = rospy.Rate(100)
     vel = Twist()
     vel_x = (np.sqrt(dvx * dvx + dvy * dvy))/1000
     endTime = rospy.Time.now() + rospy.Duration(1.5)
     while rospy.Time.now() < endTime:
         vel.linear.x = vel_x
         vel.angular.z = dw
         cmd_vel_pub_.publish(vel)
         r.sleep()
     vel.linear.x = 0
     vel.angular.z = 0
     cmd_vel_pub_.publish(vel)


#Variables
CurrentNode = []
UnvisitedNodes = []
VisitedNodes = []
CurrentIndex = 0
Rpm1 = 0
Rpm2 = 0

#Function to get Clearance,RPM
def GetParameters():
    # global Rpm1,Rpm2
    Clearance = float(input("Enter the Clearance of the robot in m: "))
    print("Enter the wheel RPM's separated by space: RPM1 RPM2")
    RPM = list(map(int, input().split()))
    Rpm1,Rpm2 = RPM[0]*3.14/30 , RPM[1]*3.14/30
    Radius = 220
    return Clearance*1000,Rpm1,Rpm2,Radius
# print(GetParameters())

#To check the given node is in Obstacle Space
def InObstacleSpace(Node):
    x = Node[0]
    y = Node[1]

    if(x**2 + y**2 <= (1000+Radius+Clearance)**2):
        return True
        Obstaclesx.append(x)
        Obstaclesy.append(y)
    elif((x+2000)**2 + (y+3000)**2 <= (1000+Radius+Clearance)**2):
        return True
        Obstaclesx.append(x)
        Obstaclesy.append(y)
    elif((x-2000)**2 + (y+3000)**2 <= (1000+Radius+Clearance)**2):
        return True
        Obstaclesx.append(x)
        Obstaclesy.append(y)
    elif((x-2000)**2 + (y-3000)**2 <= (1000+Radius+Clearance)**2):
        return True
        Obstaclesx.append(x)
        Obstaclesy.append(y)
    elif(((3750+Radius+Clearance)>=y>=(2250-Radius-Clearance)) and ((-2750-Radius-Clearance)<=x<=(-1250+Radius+Clearance))):
        return True
        Obstaclesx.append(x)
        Obstaclesy.append(y)
    elif(((750+Radius+Clearance)>=y>=(-750-Radius-Clearance)) and ((-4750-Radius-Clearance)<=x<=(-3250+Radius+Clearance))):
        return True
        Obstaclesx.append(x)
        Obstaclesy.append(y)
    elif(((750+Radius+Clearance)>=y>=(-750-Radius-Clearance)) and ((3250-Radius-Clearance)<=x<=(4750+Radius+Clearance))):
        return True
        Obstaclesx.append(x)
        Obstaclesy.append(y)
    elif((-5100)<=x<=(-5000+Radius+Clearance)):
        return True
        Obstaclesx.append(x)
        Obstaclesy.append(y)
    elif((5100)>=x>=(5000-Radius-Clearance)):
        return True
        Obstaclesx.append(x)
        Obstaclesy.append(y)
    elif((-5100)<=y<=(-5000+Radius+Clearance)):
        return True
        Obstaclesx.append(x)
        Obstaclesy.append(y)
    elif((5100)>=y>=(5000-Radius-Clearance)):
        return True
        Obstaclesx.append(x)
        Obstaclesy.append(y)
    else:
        return False
# print(InObstacleSpace([-3075.39,-2904.24]))

#Function to get the Start Position
def GetStart():
    global StartNode
    while(True):
        print("Enter the co-ordinates of starting point separated by space in m (x,y,theta(in radians) --> x y theta_s :")
        StartNode = list(map(float, input().split()))
        StartNode = [StartNode[0]*1000,StartNode[1]*1000,StartNode[2]*180/3.14]
        if(len(StartNode)==3 and not(InObstacleSpace(StartNode))):
            # StartNode = [StartNode[0],0,0,0,0]
            StartNode = [StartNode[0],StartNode[1],StartNode[2],0,0,0,0]
            # print("Start",StartNode)
            break
        else:
            print("Please provide valid starting point")
    return StartNode
# StartNode = GetStart()

#Function to get the Goal Position
def GetGoal():
    global GoalNode
    while(True):
        print("Enter the co-ordinates of goal point separated by space in m (x,y) --> x y : ")
        GoalNode = list(map(float, input().split()))
        GoalNode = [GoalNode[0]*1000,GoalNode[1]*1000]
        if len(GoalNode)==2 and not(InObstacleSpace(GoalNode)):
            break
        else:
             print("Please provide valid goal point")
    return GoalNode
# GoalNode = GetGoal()

#Function to find the Euclidean Distance between two Points
def EuclieanDistance(x2,y2,x1,y1):
    return math.sqrt((x2-x1)**2  + (y2-y1)**2)

#Function to Genrate map to plot the Obstacles
def GenerateMap():
    # print("Entered GenerateMap")
    XAll = np.linspace(-5100, 5100, num=200)
    YAll = np.linspace(-5100, 5100, num=200)
    Obstaclesx,Obstaclesy = [],[]
    for x in XAll:
        for y in YAll:
            if(x**2 + y**2 <= (1000+Radius+Clearance)**2):
                # return True
                Obstaclesx.append(x)
                Obstaclesy.append(y)
            elif((x+2000)**2 + (y+3000)**2 <= (1000+Radius+Clearance)**2):
                # return True
                Obstaclesx.append(x)
                Obstaclesy.append(y)
            elif((x-2000)**2 + (y+3000)**2 <= (1000+Radius+Clearance)**2):
                # return True
                Obstaclesx.append(x)
                Obstaclesy.append(y)
            elif((x-2000)**2 + (y-3000)**2 <= (1000+Radius+Clearance)**2):
                # return True
                Obstaclesx.append(x)
                Obstaclesy.append(y)
            elif(((3750+Radius+Clearance)>=y>=(2250-Radius-Clearance)) and ((-2750-Radius-Clearance)<=x<=(-1250+Radius+Clearance))):
                # return True
                Obstaclesx.append(x)
                Obstaclesy.append(y)
            elif(((750+Radius+Clearance)>=y>=(-750-Radius-Clearance)) and ((-4750-Radius-Clearance)<=x<=(-3250+Radius+Clearance))):
                # return True
                Obstaclesx.append(x)
                Obstaclesy.append(y)
            elif(((750+Radius+Clearance)>=y>=(-750-Radius-Clearance)) and ((3250-Radius-Clearance)<=x<=(4750+Radius+Clearance))):
                # return True
                Obstaclesx.append(x)
                Obstaclesy.append(y)
            elif((-5100)<=x<=(-5000+Radius+Clearance)):
                Obstaclesx.append(x)
                Obstaclesy.append(y)
            elif((5100)>=x>=(5000-Radius-Clearance)):
                Obstaclesx.append(x)
                Obstaclesy.append(y)
            elif((-5100)<=y<=(-5000+Radius+Clearance)):
                Obstaclesx.append(x)
                Obstaclesy.append(y)
            elif((5100)>=y>=(5000-Radius-Clearance)):
                Obstaclesx.append(x)
                Obstaclesy.append(y)

    # print("Exitting GenerateMap")
    return Obstaclesx,Obstaclesy

# Ox,Oy = GenerateMap()
# plt.show()
#Function to plot the Workspace
def GenerateWorkspace(Obstaclesx,Obstaclesy):
    plt.xlim(-5100,5100)
    plt.ylim(-5100,5100)
    plt.plot(StartNode[0], StartNode[1], "gd", markersize = '2')
    plt.plot(GoalNode[0], GoalNode[1], "gd", markersize = '2')
    plt.scatter(Obstaclesx,Obstaclesy,color = 'b')
    #plt.pause(0.001)
# GenerateWorkspace(Ox,Oy)
# plt.show()

NodeInfo = np.zeros(np.array((205,205)))  # Store visited Nodes

#Function to check if the node is already visited
def IsVisitedNode(Node):
    global NodeInfo
    if(NodeInfo[int(Node[0]/50)][int(Node[1]/50)] == 1):
    #     print("Duplicate")
        return True
    else:
        NodeInfo[int(Node[0]/50)][int(Node[1]/50)] = 1
        return False

# print(IsVisitedNode([25.01,61,178]))
# print(IsVisitedNode([25,74,-178]))

plotX =[]

#Function to add the new node to unvisited list if it is not in obstacle space and is unvisited
def AddNode(Node,px,py):
    global CurrentNode
    global UnvisitedNodes
    global plotX
    if not(InObstacleSpace(Node)) and  not(IsVisitedNode(Node)):
        UnvisitedNodes.append(Node)
        # plt.plot(px, py, color="r")
        plotX.append([px,py])
        if(len(plotX)%100 == 0):
            for i in plotX:
                plt.plot(i[0], i[1], color="r")
            #plt.pause(0.0001)
            plotX= []
        if(EuclieanDistance(GoalNode[0],GoalNode[1],Node[0],Node[1]) <= 150):
            CurrentNode = Node
            for i in plotX:
                plt.plot(i[0], i[1], color="r")
            #plt.pause(0.0001)
            plotX= []
            plt.scatter(Node[0],Node[1])
            return True
        else:
            return False
# AddNode([3.27,2.75,30,5.22,1])
# AddNode([3.4,3.1,30,0,1])

fig, ax = plt.subplots()

#Function to Genrate a new node
def GenerateNode(Node,action):
    # print(action)
    t=0
    r=33
    L=287
    dt=0.1
    Xn=Node[0]
    Yn=Node[1]
    Thetan = 3.14 * Node[2] / 180
    Cost = 0
    anim = []
# Xi, Yi,Thetai: Input point's coordinates
# Xs, Ys: Start point coordinates for plot function
# Xn, Yn, Thetan: End point coordintes
    plotx = []
    ploty = []
    while t<1.5:
        t = t + dt
        Xs = Xn
        Ys = Yn
        Xn += 0.5*r * (action[0] + action[1]) * math.cos(Thetan) * dt
        Yn += 0.5*r * (action[0] + action[1]) * math.sin(Thetan) * dt
        Thetan += (r / L) * (action[1] - action[0]) * dt
        Cost += EuclieanDistance(Xn,Yn,Xs,Ys)
        if(InObstacleSpace([Xn,Yn])):
            plotx = []
            ploty = []
            break
        plotx.append([Xs,Xn])
        ploty.append([Ys,Yn])
        # plt.plot([Xs, Xn], [Ys, Yn], color="blue")
    anim = [0.5*r * (action[0] + action[1]) * math.cos(Thetan),0.5*r * (action[0] + action[1]) * math.sin(Thetan),(r / L) * (action[1] - action[0])]
    Thetan = 180 * (Thetan) / 3.14
    CostToCome = Node[4] + Cost
    NewCost = CostToCome + EuclieanDistance(Xn,Yn,GoalNode[0],GoalNode[1])
    NewNode = [Xn,Yn,Thetan,NewCost,CostToCome,CurrentIndex,action,anim]
    return NewNode,plotx,ploty

#Function to Plot a Curve
def PlotPath(Node,action):
    t=0
    r=33
    L=287
    dt=0.1
    Xn=Node[0]
    Yn=Node[1]
    Thetan = 3.14 * Node[2] / 180
    # Cost = 0
# Xi, Yi,Thetai: Input point's coordinates
# Xs, Ys: Start point coordinates for plot function
# Xn, Yn, Thetan: End point coordintes

    while t<1.5:
        t = t + dt
        Xs = Xn
        Ys = Yn
        Xn += 0.5*r * (action[0] + action[1]) * math.cos(Thetan) * dt
        Yn += 0.5*r * (action[0] + action[1]) * math.sin(Thetan) * dt
        Thetan += (r / L) * (action[1] - action[0]) * dt

        plt.plot([Xs, Xn], [Ys, Yn], color="g")

#Action Set
actions=[[0,Rpm1],[Rpm1,0],[Rpm1,Rpm1],[0,Rpm2],[Rpm2,0],[Rpm1,Rpm2],[Rpm2,Rpm1],[Rpm2,Rpm2]]

#Function to generate possible motions based on parameters
def ActionMove(Node):
    for action in actions:
        NewNode,px,py = GenerateNode(Node,action)
        Goal = AddNode(NewNode,px,py)
        if(Goal):
            return True
    else:
        return False
# x = ActionMove(StartNode)

Path = []  #To store the path

#Function to backtrack solution path
def BackTrack(Node):
    global CurrentNode
    Path.append(Node)
    # print("Path",Path,CurrentNode)
    while(Path[0][5] != 0):
        print(VisitedNodes[Path[0][5]])
        Path.insert(0,VisitedNodes[CurrentNode[5]])
        CurrentNode=Path[0]
    Path.insert(0,VisitedNodes[0])
    plt.pause(0.001)
    return Path

ax.set_aspect('equal')
plt.title('A-Star Algorithm',fontsize=10)
Goal = False
Clearance,Rpm1,Rpm2,Radius = GetParameters()
actions=[[0,Rpm1],[Rpm1,0],[Rpm1,Rpm1],[0,Rpm2],[Rpm2,0],[Rpm1,Rpm2],[Rpm2,Rpm1],[Rpm2,Rpm2]]
X,Y = GenerateMap()
StartNode = GetStart()
GoalNode = GetGoal()
GenerateWorkspace(X,Y)
StartTime = time.time()
CurrentNode = copy.deepcopy(StartNode)
UnvisitedNodes.append(CurrentNode)
while(1):
    VisitedNodes.append(UnvisitedNodes.pop(0))
    Goal = ActionMove(CurrentNode)
    UnvisitedNodes.sort(key = lambda x: x[3])
    if(len(UnvisitedNodes)>4000):                                 #Removing Old nodes with higher cost to reduce the runtime
        UnvisitedNodes = UnvisitedNodes[:3000]
        print("Deleting")
    if(Goal):
        print("Goal",CurrentNode)
        break
    CurrentIndex += 1
    CurrentNode = UnvisitedNodes[0]
if(Goal):
    Path = BackTrack(CurrentNode)
    print("PAth",Path)
    for i in range(len(Path)-1):
        PlotPath(Path[i],Path[i+1][6])
    plt.pause(0.001)
    EndTime = time.time()
    print("Solved" , EndTime - StartTime)
Path.pop(0)
for i in Path:
    j = i[7]
    move_robot(cmd_vel_pub_, j[0], j[1],j[2])
vel = Twist()
vel.linear.x = 0
vel.angular.z = 0
cmd_vel_pub_.publish(vel)
plt.show()
#plt.close()
