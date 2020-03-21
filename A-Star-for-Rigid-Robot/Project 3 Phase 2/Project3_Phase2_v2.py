import numpy as np
import matplotlib.pyplot as plt
import copy
import math
import time

#Variables
StartNode = [50,50,0,0,0]
GoalNode = [150,150]
CurrentNode = []
UnvisitedNodes = []
VisitedNodes = []
CurrentIndex = 0
Clearance = 1
Radius = 1
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


# print(InObstacleSpace([3.27,2.75]))

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
        NodeInfo[int(TempX*2)][int(TempY*2)][int(TempTheta)]=1
        return False
    # # if (Node[2] is not 0):
    #
    # NewNode = [TempX,TempY,TempTheta,Node[3],Node[4]]
    # print("Node",Node,"Thresholded",NewNode)
# print(IsVisitedNode([3.27,2.75,30,5.22,1]))
# print(IsVisitedNode([3.4,3.1,30,0,1]))

def AddNode(Node):
    global CurrentNode
    global UnvisitedNodes
    # print("Node",Node,"Obstacle",InObstacleSpace(Node),"Visited",IsVisitedNode(Node))
    if not(InObstacleSpace(Node)) and  not(IsVisitedNode(Node)):
        # print("AddingNode")
        UnvisitedNodes.append(Node)
        ax.quiver(CurrentNode[0], CurrentNode[1], Node[0]-CurrentNode[0], Node[1]-CurrentNode[1],units='xy' ,scale=1)
        # plt.pause(0.001)
        if(EuclieanDistance(GoalNode[0],GoalNode[1],Node[0],Node[1]) <= 1.5):
            # VisitedNodes.append(CurrentNode)
            ax.quiver(CurrentNode[0], CurrentNode[1], Node[0]-CurrentNode[0], Node[1]-CurrentNode[1],units='xy' ,scale=1,color = 'r')
            CurrentNode = Node
            return True
        else:
            return False



# AddNode([3.27,2.75,30,5.22,1])
# AddNode([3.4,3.1,30,0,1])
# print(UnvisitedNodes)
fig, ax = plt.subplots()


def ActionMove(Node):
    PossibleMoves = int(360/Theta)
    # print("Possible Moves",PossibleMoves)
    NewList = []
    for i in range(PossibleMoves):
        NewTheta = i*Theta
        NewX = Node[0] + StepSize*(math.cos(math.radians(NewTheta)))
        NewY = Node[1] + StepSize*(math.sin(math.radians(NewTheta)))
        CostNode = EuclieanDistance(NewX,NewY,StartNode[0],StartNode[1]) + EuclieanDistance(NewX,NewY,GoalNode[0],GoalNode[1])
        NewCost = CostNode
        NewNode = [round(NewX,2),round(NewY,2),int(NewTheta),round(NewCost,2),CurrentIndex]
        Goal = AddNode(NewNode)
        if(Goal):
            return True
    else:
        return False

# def GeneratePath(CurrentNode):
#     global CurrentNodeIndex
#     Path.append(CurrentNodeIndex)
#     while(Path[0] != 0):
#         Path.insert(0,ParentNodeIndex[node.index(CurrentNode)])
#         CurrentNode = node[Path[0]]
#
#     for i in range(len(Path)):
#         NodePath.append(node[Path[i]])
Path = []
def BackTrack(Node):
    global CurrentNode
    Path.append(Node)
    print("Path",Path)
    while(Path[0][4] != 0):
        print(VisitedNodes[Path[0][4]])
        Path.insert(0,VisitedNodes[CurrentNode[4]])
        ax.quiver(Path[0][0], Path[0][1], CurrentNode[0]-Path[0][0], CurrentNode[1]-Path[0][1],  units='xy' ,scale=1,color = 'r')

        # ax.quiver(CurrentNode[0],CurrentNode[1],Path[0][0]-CurrentNode[0], Path[0][1]-CurrentNode[1],  units='xy' ,scale=1,color = 'r')
        # plt.pause(0.1)
        CurrentNode=Path[0]
    Path.insert(0,VisitedNodes[0])
    ax.quiver(Path[0][0], Path[0][1], CurrentNode[0]-Path[0][0], CurrentNode[1]-Path[0][1],  units='xy' ,scale=1,color = 'r')

    print(Path)
    return Path





plt.grid()

ax.set_aspect('equal')

plt.xlim(0,300)
plt.ylim(0,200)

plt.title('How to plot a vector in matplotlib ?',fontsize=10)
Goal = False


# AddNodes(NewList)
# print("Unvisited",UnvisitedNodes)
# plt.matshow(Info)
# plt.show()
#
print("Length",len(UnvisitedNodes), "Unvisited",UnvisitedNodes)
CurrentNode = copy.deepcopy(StartNode)
print("CurrentIndex",CurrentIndex,"Node",CurrentNode)
UnvisitedNodes.append(CurrentNode)
while(1):
    VisitedNodes.append(UnvisitedNodes.pop(0))
    Goal = ActionMove(CurrentNode)
    UnvisitedNodes.sort(key = lambda x: x[3])
    if(Goal):
        print("Goal",CurrentNode)
        break

    CurrentIndex += 1
    CurrentNode = UnvisitedNodes[0]
    print("CurrentIndex",CurrentIndex,"Node",CurrentNode)
    # print("UnvisitedNodes",UnvisitedNodes)
    # print("VisitedNodes",VisitedNodes)
Path = BackTrack(CurrentNode)
print(Path)
#
#
plt.savefig('how_to_plot_a_vector_in_matplotlib_fig3.png', bbox_inches='tight')
#
print("SAved")
# plt.show()
plt.close()
