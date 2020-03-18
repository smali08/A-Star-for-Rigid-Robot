import numpy as np
import matplotlib.pyplot as plot
import copy
import math
import time

#Variables
StartNode = []
GoalNode = []
CurrentNode = []
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

def ActionMove(Node,Theta):
    
