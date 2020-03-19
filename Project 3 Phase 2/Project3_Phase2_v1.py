import numpy as np
import matplotlib.pyplot as plt
import copy
import math
import time

#Variables
StartNode = [2,2,0,0,0]
GoalNode = [5,5]
CurrentNode = []
UnvisitedNodes = []
VisitedNodes = []
CurrentIndex = 0
Clearance = 0
Radius = 0
StepSize = 1
Theta = 30


def GetParameters():
    global Radius
    global Clearance
    global StepSize
    global Theta
    Radius = int(input("Enter the Radius of the robot: "))
    Clearance = int(input("Enter the Clearance of the robot: "))
    StepSize = int(input("Enter the step-size of movement: "))
    Theta = int(input("Enter the angle between two consecutive actions "))
    return Radius,Clearance,StepSize,Theta

def GetStart():
    global StartNode
    while(True):
        print("Enter the co-ordinates of starting point separated by space  (x,y,theta_s) --> x y theta_s:")
        StartNode = list(map(int, input().split()))
        if (len(StartNode)==3) and not(InObstacleSpace(StartNode)):
            break
        else:
            print("Please provide valid starting point")
    return StartNode

def GetGoal():
    global GoalNode
    while(True):
        print("Enter the co-ordinates of goal point separated by space  (x,y,theta_g) --> x y theta_g: ")
        GoalNode = list(map(int, input().split()))
        if len(GoalNode)==3 and not(InObstacleSpace(GoalNode)):
            break
        else:
             print("Please provide valid goal point")
    return GoalNode

def EuclieanDistance(x2,y2,x1,y1):
    return math.sqrt((x2-x1)**2  + (y2-y1)**2)

def InObstacleSpace(Node):
    x = Node[0]
    y = Node[1]
    if((x-225)**2 + (y-150)**2 <= (25 + Clearance + Radius)**2):
        return True
        Map[200-y][x] = 1
        Obstaclesx.append(x)
        Obstaclesy.append(y)
    if(((x-150)**2/(40 + Clearance + Radius)**2 + (y-100)**2/(20 + Clearance + Radius)**2) <= 1):
        return True
        Map[200-y][x] = 1
        Obstaclesx.append(x)
        Obstaclesy.append(y)
    if ((y-(0.6*x))>=(-125 - Clearance - Radius) and (y-(-0.6*x))<=(175 + Clearance + Radius) and (y-(0.6*x))<=(-95 + Clearance + Radius) and (y-(-0.6*x))>=(145 - Clearance - Radius)):
        return True
        Map[200-y][x] = 1
        Obstaclesx.append(x)
        Obstaclesy.append(y)
    if((y-(13*x))<=(-140 + Clearance + Radius) and (y-(1*x))>=(100 - Clearance - Radius) and y <= (185 + Clearance + Radius) and (y-(1.4*x)>=(80 - Clearance - Radius))):
        return True
        Map[200-y][x] = 1
        Obstaclesx.append(x)
        Obstaclesy.append(y)
    if ((y-(-1.2*x))>=(210 - Clearance - Radius) and (y-(1.2*x))>=(30 - Clearance - Radius) and (y-(-1.4*x))<=(290 + Clearance + Radius) and (y-(-2.6*x))>=(280 - Clearance - Radius) and y<=(185 + Clearance + Radius)):
        return True
        Map[200-y][x] = 1
        Obstaclesx.append(x)
        Obstaclesy.append(y)
    if ((y - (1.73)*x + 135 >= 0 - Clearance - Radius) and (y + (0.58)*x - 96.35  <= 0 + Clearance + Radius) and (y - (1.73)*x - 15.54 <= 0 + Clearance + Radius) and (y + (0.58)*x - 84.81 >= 0 - Clearance - Radius)):
        return True
        Map[200-y][x] = 1
        Obstaclesx.append(x)
        Obstaclesy.append(y)
    if ((y <=  Clearance + Radius)):
        return True
        Map[200-y][x] = 1
        Obstaclesx.append(x)
        Obstaclesy.append(y)
    if ((x <= Clearance + Radius)):
        return True
        Map[200-y][x] = 1
        Obstaclesx.append(x)
        Obstaclesy.append(y)
    if ((x >= 300  - (Clearance + Radius)  )):
        return True
        Map[200 - y][x] = 1
        Obstaclesx.append(x)
        Obstaclesy.append(y)
    if ((200 >= y >=  200 - (Clearance + Radius))):
        return True
        Map[200-y][x] = 1
        Obstaclesx.append(x)
        Obstaclesy.append(y)
    else:
        return False


# print(InObstacleSpace([50,186]))

NodeInfo = np.zeros(np.array((601,401,12)))

def IsVisitedNode(Node):
    global NodeInfo
    TempX = Node[0] % 0.5
    TempY = Node[1] % 0.5
    TempTheta = int(Node[2]/Theta)
    if(TempX < 0.25):
        TempX = Node[0] - TempX
    else:
        TempX = Node[0] + (0.5-TempX)
    if(TempY < 0.25):
        TempY = Node[1] - TempY
    else:
        TempY = Node[1] + (0.5-TempY)

    if(NodeInfo[int(TempX*2)][int(TempY*2)][int(TempTheta)] == 1):
        return True
    else:
        return False


    # # if (Node[2] is not 0):
    #
    # NewNode = [TempX,TempY,TempTheta,Node[3],Node[4]]
    # print("Node",Node,"Thresholded",NewNode)
IsVisitedNode([3.27,2.75,30,5.22,1])


fig, ax = plt.subplots()
def ActionMove(Node):
    global Theta
    global GoalNode
    global CurrentIndex
    PossibleMoves = int(360/Theta)
    # print("Possible Moves",PossibleMoves)
    NewList = []
    for i in range(PossibleMoves):
        NewTheta = i*Theta
        NewX = Node[0] + StepSize*(math.cos(math.radians(NewTheta)))
        NewY = Node[1] + StepSize*(math.sin(math.radians(NewTheta)))
        CostNode = EuclieanDistance(NewX,NewY,Node[0],Node[1]) + EuclieanDistance(NewX,NewY,GoalNode[0],GoalNode[1])
        NewCost = Node[3] + CostNode
        NewNode = [round(NewX,2),round(NewY,2),int(NewTheta),round(NewCost,2),CurrentIndex]
        NewList.append(NewNode)
        # print("Angle",i*Theta,"NewNode",NewNode,"Parent",Node)
        # ax.quiver(Node[0], Node[1], NewNode[0]-Node[0], NewNode[1]-Node[1],units='xy' ,scale=1)
    print("NewList",NewList)
    # NewList.sort(key = lambda x: x[3])
    # print("Sorted",NewList)
    # plt.show()
    return NewList
# NewList = ActionMove(StartNode)
# UnvisitedNodes.append(StartNode)

# plt.grid()
#
# ax.set_aspect('equal')
#
# plt.xlim(0,5)
# plt.ylim(0,5)
#
# plt.title('How to plot a vector in matplotlib ?',fontsize=10)
# Goal = False
def AddNodes(List):
    global Goal
    global CurrentNode
    global Theta
    global Info
    global UnvisitedNodes
    ListCopy = copy.deepcopy(List)
    for n,i in enumerate(ListCopy):
        if(0 <= i[0]-math.floor(i[0]) < 0.25):
            i[0] = math.floor(i[0])
        elif(0.25 <= i[0]-math.floor(i[0]) < 0.75):
            i[0] = math.floor(i[0]) + 0.5
        else:
            i[0] = math.ceil(i[0])
        if(0 <= i[1]-math.floor(i[1]) < 0.25):
            i[1] = math.floor(i[1])
        elif(0.25 <= i[1]-math.floor(i[1]) < 0.75):
            i[1] = math.floor(i[1]) + 0.5
        else:
            i[1] = math.ceil(i[1])
        if(i[2] is not 0):
            i[2] = i[2]/Theta
        if(Info[int(2*i[0])][int(2*i[1])][int(i[2])] == 0):
            Info[int(2*i[0])][int(2*i[1])][int(i[2])] = 1
            UnvisitedNodes.append(List[n])
            if(EuclieanDistance(GoalNode[0],GoalNode[1],List[n][0],List[n][1]) <= 1.5):
                Goal = True

            ax.quiver(CurrentNode[0], CurrentNode[1], List[n][0]-CurrentNode[0], List[n][1]-CurrentNode[1],units='xy' ,scale=1)
            plt.pause(0.001)
        else:
            print("Duplicate",i)
        if(Goal):
            CurrentNode = List[n]
    print("Length",len(UnvisitedNodes), "Unvisited",UnvisitedNodes)
    UnvisitedNodes.sort(key = lambda x: x[3])
    print("Sorted",UnvisitedNodes)


# AddNodes(NewList)
# print("Unvisited",UnvisitedNodes)
# plt.matshow(Info)
# plt.show()
#
# CurrentIndex=0
# print("Length",len(UnvisitedNodes), "Unvisited",UnvisitedNodes)
# CurrentNode = copy.deepcopy(StartNode)
# print("CurrentIndex",CurrentIndex,"Node",CurrentNode)
# UnvisitedNodes.append(CurrentNode)
# while not(Goal):
#     VisitedNodes.append(UnvisitedNodes.pop(0))
#     NewNodes = ActionMove(CurrentNode)
#     AddNodes(NewNodes)
#     if(Goal):
#         print(CurrentNode)
#         break
#     CurrentIndex += 1
#     CurrentNode = UnvisitedNodes[0]
#     print("CurrentIndex",CurrentIndex,"Node",CurrentNode)
#
#
# # plt.savefig('how_to_plot_a_vector_in_matplotlib_fig3.png', bbox_inches='tight')
#
# plt.show()
# plt.close()
