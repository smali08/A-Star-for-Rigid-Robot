import numpy as np
import matplotlib.pyplot as plt
import copy
import math
import time

#Variables
Workspace = [10200,10200]
CurrentNode = []
UnvisitedNodes = []
VisitedNodes = []
CurrentIndex = 0

Radius = 354/2
Clearance = 0
#Function to get Radius, Clearance, Step-size and Theta values
def GetParameters():
    Clearance = int(input("Enter the Clearance of the robot: "))
    print("Enter the wheel RPM's separated by space: RPM1 RPM2")
    RPM = list(map(int, input().split()))
    Radius = 354/2
    return Clearance,RPM,Radius
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
    # if(x**2 + y**2 <= 1000):
    #     return True
    #     Obstaclesx.append(x)
    #     Obstaclesy.append(y)
    # elif((x-3100)**2 + (y-2100) <= 1000):
    #     return True
    #     Obstaclesx.append(x)
    #     Obstaclesy.append(y)
    # elif((x-7100)**2 + (y-2100) <= 1000):
    #     return True
    #     Obstaclesx.append(x)
    #     Obstaclesy.append(y)
    # elif((x-7100)**2 + (y-8100) <= 1000):
    #     return True
    #     Obstaclesx.append(x)
    #     Obstaclesy.append(y)
    # # elif((x-3100)**2 + (y-2100) <= 1000):
    # #     return True
    # #     Obstaclesx.append(x)
    # #     Obstaclesy.append(y)
    # elif((8850>=y>=7350) and (3850>=x>=2350)):
    #     return True
    #     Obstaclesx.append(x)
    #     Obstaclesy.append(y)
    # elif((5850>=y>=4350) and (1850>=x>=350)):
    #     return True
    #     Obstaclesx.append(x)
    #     Obstaclesy.append(y)
    # elif((5850>=y>=4350) and (9850>=x>=8350)):
    #     return True
    #     Obstaclesx.append(x)
    #     Obstaclesy.append(y)
    #
    #
    # if(x**2 + y**2 <= 1000):
    #     return True
    #     Obstaclesx.append(x)
    #     Obstaclesy.append(y)
    # elif((x+2000)**2 + (y+3000) <= 1000):
    #     return True
    #     Obstaclesx.append(x)
    #     Obstaclesy.append(y)
    # elif((x-2000)**2 + (y+3000) <= 1000):
    #     return True
    #     Obstaclesx.append(x)
    #     Obstaclesy.append(y)
    # elif((x-2000)**2 + (y-3000) <= 1000):
    #     return True
    #     Obstaclesx.append(x)
    #     Obstaclesy.append(y)
    # elif((3750>=y>=2250) and (-2750>=x>=-1250)):
    #     return True
    #     Obstaclesx.append(x)
    #     Obstaclesy.append(y)
    # elif((750>=y>=-750) and (-4750>=x>=-3250)):
    #     return True
    #     Obstaclesx.append(x)
    #     Obstaclesy.append(y)
    # elif((750>=y>=-750) and (3250>=x>=4750)):
    #     return True
    #     Obstaclesx.append(x)
    #     Obstaclesy.append(y)

    # if ((y-(-1.2*x))>=(210 - Clearance - Radius) and (y-(1.2*x))>=(30 - Clearance - Radius) and (y-(-1.4*x))<=(290 + Clearance + Radius) and (y-(-2.6*x))>=(280 - Clearance - Radius) and y<=(185 + Clearance + Radius)):
    #     return True
    #     Obstaclesx.append(x)
    #     Obstaclesy.append(y)
    # elif ((y - (1.73)*x + 135 >= 0 - Clearance - Radius) and (y + (0.58)*x - 96.35  <= 0 + Clearance + Radius) and (y - (1.73)*x - 15.54 <= 0 + Clearance + Radius) and (y + (0.58)*x - 84.81 >= 0 - Clearance - Radius)):
    #     return True
    #     Obstaclesx.append(x)
    #     Obstaclesy.append(y)
    # elif((x-225)**2 + (y-150)**2 <= (25 + Clearance + Radius)**2):
    #     return True
    #     Obstaclesx.append(x)
    #     Obstaclesy.append(y)
    # elif(((x-150)**2/(40 + Clearance + Radius)**2 + (y-100)**2/(20 + Clearance + Radius)**2) <= 1):
    #     return True
    #     Obstaclesx.append(x)
    #     Obstaclesy.append(y)
    # elif ((y-(0.6*x))>=(-125 - Clearance - Radius) and (y-(-0.6*x))<=(175 + Clearance + Radius) and (y-(0.6*x))<=(-95 + Clearance + Radius) and (y-(-0.6*x))>=(145 - Clearance - Radius)):
    #     return True
    #     Obstaclesx.append(x)
    #     Obstaclesy.append(y)
    # elif((y-(13*x))<=(-140 + Clearance + Radius) and (y-(1*x))>=(100 - Clearance - Radius) and y <= (185 + Clearance + Radius) and (y-(1.4*x)>=(80 - Clearance - Radius))):
    #     return True
    #     Obstaclesx.append(x)
    #     Obstaclesy.append(y)
    # elif ((y <=  Clearance + Radius)):
    #     return True
    #     Obstaclesx.append(x)
    #     Obstaclesy.append(y)
    # elif ((x <= Clearance + Radius)):
    #     return True
    #     Obstaclesx.append(x)
    #     Obstaclesy.append(y)
    # elif ((x >= 300  - (Clearance + Radius)  )):
    #     return True
    #     Obstaclesx.append(x)
    #     Obstaclesy.append(y)
    # elif ((200 >= y >=  200 - (Clearance + Radius))):
    #     return True
    #     Obstaclesx.append(x)
    #     Obstaclesy.append(y)
    else:
        return False

# print(InObstacleSpace([0,-]))
#Function to get the Start Position
def GetStart():
    global StartNode
    while(True):
        print("Enter the co-ordinates of starting point separated by space  (x,y,theta_s) --> x y theta_s:")
        StartNode = list(map(int, input().split()))
        if(len(StartNode)==3 and not(InObstacleSpace(StartNode))):
            # StartNode = [StartNode[0] + StepSize*(math.cos(math.radians(StartNode[2]))),StartNode[1] + StepSize*(math.sin(math.radians(StartNode[2]))),0,0,0,0]
        # print("Start",StartNode)
            break
        else:
            print("Please provide valid starting point")
    return StartNode

StartNode = GetStart()
#Function to get the Goal Position
def GetGoal():
    global GoalNode
    while(True):
        print("Enter the co-ordinates of goal point separated by space  (x,y) --> x y : ")
        GoalNode = list(map(int, input().split()))
        # StartNode = [GoalNode[0] + StepSize*(math.cos(math.radians(StartNode[2]))),GoalNode[1] + StepSize*(math.sin(math.radians(GoalNode[2]))),]
        if len(GoalNode)==2 and not(InObstacleSpace(GoalNode)):
            break
        else:
             print("Please provide valid goal point")
    return GoalNode
GoalNode = GetGoal()
#Function to find the Euclidean Distance between two Points
def EuclieanDistance(x2,y2,x1,y1):
    return math.sqrt((x2-x1)**2  + (y2-y1)**2)




#Function to Genrate map to plot the Obstacles
def GenerateMap():
    print("Entered GenerateMap")
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

    print("Exitting GenerateMap")
    return Obstaclesx,Obstaclesy

Ox,Oy = GenerateMap()
# plt.show()
#Function to plot the Workspace
def GenerateWorkspace(Obstaclesx,Obstaclesy):
    plt.xlim(-5100,5100)
    plt.ylim(-5100,5100)
    plt.plot(StartNode[0], StartNode[1], "gd", markersize = '2')
    plt.plot(GoalNode[0], GoalNode[1], "gd", markersize = '2')
    plt.scatter(Obstaclesx,Obstaclesy,color = 'b')
    # plt.pause(10)
GenerateWorkspace(Ox,Oy)
plt.show()
NodeInfo = np.zeros(np.array((205,205,11)))  # Store visited Nodes

#Function to check if the node is already visited
def IsVisitedNode(Node):
    global NodeInfo
    print("Temp1",[round(Node[0]/50),round(Node[1]/50),round(Node[2]/36)])
    TempX = Node[0] % 50
    TempY = Node[1] % 50
    TempTheta = round((Node[2]/36),0)
    print(TempTheta)
    if(TempX < 25):
        TempX = Node[0] - TempX
    else:
        TempX = Node[0] + (50-TempX)
    if(TempY < 25):
        TempY = Node[1] - TempY
    else:
        TempY = Node[1] + (50-TempY)
    print("Temp",[TempX,TempY,TempTheta])
    print([int(TempX/50),int(TempY/50),int(TempTheta)])
    if(NodeInfo[int(TempX/50)][int(TempY/50)][int(TempTheta)] == 1):
        # print("Duplicate")
        return True
    else:
        NodeInfo[int(TempX/50)][int(TempY/50)][int(TempTheta)]=1
        return False

print(IsVisitedNode([26,61,178]))
print(IsVisitedNode([32,74,-178]))
# print(IsVisitedNode([]))
plotX,plotY,plotX2,plotY2 = [],[],[],[]

#Function to add the new node to unvisited list if it is not in obstacle space and is unvisited
def AddNode(Node):
    global CurrentNode
    global UnvisitedNodes
    global plotX,plotY,plotX2,plotY2
    if not(InObstacleSpace(Node)) and  not(IsVisitedNode(Node)):
        UnvisitedNodes.append(Node)
        # plotX.append(CurrentNode[0])
        # plotY.append(CurrentNode[1])
        # plotX2.append( Node[0]-CurrentNode[0] )
        # plotY2.append( Node[1]-CurrentNode[1] )
        # if(len(plotX)%5000 == 0):
        #     ax.quiver(plotX, plotY, plotX2, plotY2,units='xy' ,scale=1)
        #     plt.pause(0.001)
        #     plotX,plotY,plotX2,plotY2 = [],[],[],[]
        # ax.quiver(CurrentNode[0], CurrentNode[1], Node[0]-CurrentNode[0], Node[1]-CurrentNode[1],units='xy' ,scale=1)
        # plt.pause(0.001)
        if(EuclieanDistance(GoalNode[0],GoalNode[1],Node[0],Node[1]) <= 1.5 and Node[2]==GoalNode[2]):
            # ax.quiver(CurrentNode[0], CurrentNode[1], Node[0]-CurrentNode[0], Node[1]-CurrentNode[1],units='xy' ,scale=1,color = 'r')
            CurrentNode = Node
            ax.quiver(plotX, plotY, plotX2, plotY2,units='xy' ,scale=1)
            plt.pause(0.001)
            plotX,plotY,plotX2,plotY2 = [],[],[],[]
            return True
        else:
            return False

# AddNode([3.27,2.75,30,5.22,1])
# AddNode([3.4,3.1,30,0,1])
# print(UnvisitedNodes)
fig, ax = plt.subplots()

#Function to generate possible motions based on parameters
def ActionMove(Node):
    PossibleMoves = int(360/Theta)

    for i in range(PossibleMoves):
        NewTheta = i*Theta
        NewX = Node[0] + StepSize*(math.cos(math.radians(NewTheta)))
        NewY = Node[1] + StepSize*(math.sin(math.radians(NewTheta)))

        # CostToCome = Node[5] + EuclieanDistance(NewX,NewY,Node[0],Node[1])
        CostToCome = Node[5] + 1
        NewCost = CostToCome + EuclieanDistance(NewX,NewY,GoalNode[0],GoalNode[1])

        # CostNode = CostToCome + EuclieanDistance(NewX,NewY,GoalNode[0],GoalNode[1])
        # NewCost = CostNode
        NewNode = [round(NewX,2),round(NewY,2),int(NewTheta),NewCost,CurrentIndex,CostToCome]
        Goal = AddNode(NewNode)
        if(Goal):
            return True
    else:
        return False

Path = []  #To store the path

#Function to backtrack and plot path
def BackTrack(Node):
    global CurrentNode
    Path.append(Node)
    print("Path",Path,CurrentNode)
    while(Path[0][4] != 0):
        print(VisitedNodes[Path[0][4]])
        Path.insert(0,VisitedNodes[CurrentNode[4]])
        print("NewPAth")
        ax.quiver(Path[0][0], Path[0][1], CurrentNode[0]-Path[0][0], CurrentNode[1]-Path[0][1],  units='xy' ,scale=1,color = 'r')
        CurrentNode=Path[0]
    Path.insert(0,VisitedNodes[0])
    ax.quiver(Path[0][0], Path[0][1], CurrentNode[0]-Path[0][0], CurrentNode[1]-Path[0][1],  units='xy' ,scale=1,color = 'r')
    plt.pause(0.001)
    return Path

# plt.grid()
# ax.set_aspect('equal')
# plt.xlim(0,300)
# plt.ylim(0,200)
# plt.title('A-Star Algorithm',fontsize=10)
# Goal = False
# Radius,Clearance,StepSize,Theta = GetParameters()
# X,Y = GenerateMap()
# StartNode = GetStart()
# GoalNode = GetGoal()
# GenerateWorkspace(X,Y)
# StartTime = time.time()
# # print("Length",len(UnvisitedNodes), "Unvisited",UnvisitedNodes)
# CurrentNode = copy.deepcopy(StartNode)
# # print("CurrentIndex",CurrentIndex,"Node",CurrentNode)
# UnvisitedNodes.append(CurrentNode)
# while(1):
#     # VisitedNodes.append(UnvisitedNodes.remove(CurrentNode))
#     VisitedNodes.append(UnvisitedNodes.pop(0))
#     Goal = ActionMove(CurrentNode)
#     # print("Lenght",len(UnvisitedNodes))
#     UnvisitedNodes.sort(key = lambda x: x[3])
#     if(len(UnvisitedNodes)>4000):                                 #Removing Old nodes with higher cost to reduce the runtime
#         UnvisitedNodes = UnvisitedNodes[:3000]
#     if(Goal):
#         print("Goal",CurrentNode)
#         break
#     elif(len(UnvisitedNodes) == 0):
#         print(" No SOlution")
#         break
#
#     CurrentIndex += 1
#     CurrentNode = UnvisitedNodes[0]
#
# EndTime = time.time()
# if(Goal):
#     print("Solved" , EndTime - StartTime)
#     Path = BackTrack(CurrentNode)
#     print(Path)
#     EndTime = time.time()
#     print("Solved" , EndTime - StartTime)
# plt.show()
# plt.close()
