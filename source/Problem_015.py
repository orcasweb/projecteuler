'''
Created on Jan 15, 2019

@author: orcasweb
'''
from math import factorial
gridSize = 20
paths = 0


def goRight(x, y):
    if(canGoRightTF(x, y)):
        y = y + 1


def goDown(x, y):
    if(canGoDownTF(x, y)):
        x = x + 1


def canGoRightTF(x, y):
    if(y + 1 <= gridSize):
        return True


def canGoDownTF(x, y):
    if(x + 1 <= gridSize):
        return True


def getNexPointListRecursive(x, y):
    global paths
    if((x == gridSize) & (y == gridSize)):
        paths = paths + 1
    if(canGoRightTF(x, y)):
        getNexPointListRecursive(x, y + 1)
    if(canGoDownTF(x, y)):
        getNexPointListRecursive(x + 1, y)

def getPathsforGrid(size):
    pathLength = 2*size
    pathsgs = int(factorial(pathLength)/(factorial(size)*factorial(pathLength-size)))
    return pathsgs
    
    
#getNexPointListRecursive(0, 0)
#print("The number of paths is: ", paths)
pathsgs = getPathsforGrid(gridSize)
print("The number of paths is: ", pathsgs)
