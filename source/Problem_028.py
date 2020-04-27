'''
Created on Apr 25, 2020

@author: orcasweb
'''
'''
Note that i solved this in two ways. First one is by building the matrix. 
Second is by mathematical analysis
'''
import numpy as np

matrixSize = 1001


def getMoves(size):
    ESWNMovesList = []
    for i in range(1, size):
        ESWNMovesList.append(i)
        ESWNMovesList.append(i)
    ESWNMovesList.append(size - 1)
    return ESWNMovesList

# print(getMoves(matrixSize))


def getMatrixMoves(ESWNMoves):
    r = divmod(matrixSize, 2)[0]
    c = divmod(matrixSize, 2)[0]
    matrixMovesList = []
    for move in range(0, len(ESWNMoves)):
        if(move % 4 == 0):
            for i in range(0, ESWNMoves[move]):
                c = c + 1
                matrixMovesList.append([r, c])
#             print(r, c)
        elif(move % 4 == 1):
            for i in range(0, ESWNMoves[move]):
                r = r + 1
                matrixMovesList.append([r, c])
#             print(r, c)
        elif(move % 4 == 2):
            for i in range(0, ESWNMoves[move]):
                c = c - 1
                matrixMovesList.append([r, c])
#             print(r, c)
        elif(move % 4 == 3):
            for i in range(0, ESWNMoves[move]):
                r = r - 1
                matrixMovesList.append([r, c])
#             print(r, c)
    return matrixMovesList
            
# print(getMatrixMoves(getMoves(matrixSize)))


matrixMovesList = getMatrixMoves(getMoves(matrixSize))

mainMatrix = np.zeros((matrixSize, matrixSize))
# print(mainMatrix)

startRow = divmod(matrixSize, 2)[0]
startCol = divmod(matrixSize, 2)[0]
mainMatrix[(startRow, startCol)] = 1
currValue = 1
for li in matrixMovesList:
    mainMatrix[(li[0], li[1])] = currValue + 1
    currValue = currValue + 1
# print(mainMatrix)

# get the diagonal sum
diagSum = 0
for i in range(0, matrixSize):
    diagSum = diagSum + mainMatrix[i, i]
    diagSum = diagSum + mainMatrix[i, matrixSize - 1 - i]
diagSum = diagSum - mainMatrix[startRow, startCol]

print("The diagonals sum is: ", int(diagSum))

print("Solving using the mathematical analysis....")

# start with diagSum = 1 because this is the center
# the four corners are derived using the formula
diagSum = 1
# each iteration the four corners are calculated and added cumulatively
for x in range(3, matrixSize + 1, 2):
    TR = (x ** 2)
    TL = (x ** 2) - (x * 1) + 1
    BL = (x ** 2) - (x * 2) + 2
    BR = (x ** 2) - (x * 3) + 3
    diagSum = diagSum + TR + TL + BL + BR

print("The diagonals sum is: ", int(diagSum))
