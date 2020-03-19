import numpy as np
import matplotlib.pyplot as plt
import copy
import math
import time

#Variables
StartNode = [2,2,0,0]
GoalNode = [5,5]
CurrentNode = []
UnvisitedNodes = []
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
    Radius = int(input("Enter the radius of the robot: "))
    Clearance = int(input("Enter the clearance of the robot: "))
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


fig, ax = plt.subplots()
def ActionMove(Node):
    global Theta
    global GoalNode
    PossibleMoves = int(360/Theta)
    # print("Possible Moves",PossibleMoves)
    NewList = []
    for i in range(PossibleMoves):
        NewTheta = i*Theta
        NewX = Node[0] + StepSize*(math.cos(math.radians(NewTheta)))
        NewY = Node[1] + StepSize*(math.sin(math.radians(NewTheta)))
        CostNode = EuclieanDistance(NewX,NewY,Node[0],Node[1]) + EuclieanDistance(NewX,NewY,GoalNode[0],GoalNode[1])
        NewCost = Node[3] + CostNode
        NewNode = [round(NewX,2),round(NewY,2),int(NewTheta),round(NewCost,2)]
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
Info = np.zeros(np.array((601,401,12)))


plt.grid()

ax.set_aspect('equal')

plt.xlim(0,5)
plt.ylim(0,5)

plt.title('How to plot a vector in matplotlib ?',fontsize=10)
Goal = False
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

    print("Length",len(UnvisitedNodes), "Unvisited",UnvisitedNodes)
    UnvisitedNodes.sort(key = lambda x: x[3])
    print("Sorted",UnvisitedNodes)


# AddNodes(NewList)
# print("Unvisited",UnvisitedNodes)
# plt.matshow(Info)
# plt.show()

CurrentIndex=0
print("Length",len(UnvisitedNodes), "Unvisited",UnvisitedNodes)
CurrentNode = copy.deepcopy(StartNode)
print("CurrentIndex",CurrentIndex,"Node",CurrentNode)
UnvisitedNodes.append(CurrentNode)
while not(Goal):
    NewNodes = ActionMove(CurrentNode)
    AddNodes(NewNodes)
    CurrentIndex += 1
    CurrentNode = UnvisitedNodes[CurrentIndex]
    print("CurrentIndex",CurrentIndex,"Node",CurrentNode)


# plt.savefig('how_to_plot_a_vector_in_matplotlib_fig3.png', bbox_inches='tight')

plt.show()
plt.close()
