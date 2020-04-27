'''
Created on Apr 25, 2020

@author: orcasweb
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
    for move in range(0,len(ESWNMoves)):
        if(move % 4 == 0):
            for i in range(0,ESWNMoves[move]):
                c = c + 1
                matrixMovesList.append([r,c])
#             print(r, c)
        elif(move % 4 == 1):
            for i in range(0,ESWNMoves[move]):
                r = r + 1
                matrixMovesList.append([r,c])
#             print(r, c)
        elif(move % 4 == 2):
            for i in range(0,ESWNMoves[move]):
                c = c - 1
                matrixMovesList.append([r,c])
#             print(r, c)
        elif(move % 4 == 3):
            for i in range(0,ESWNMoves[move]):
                r = r - 1
                matrixMovesList.append([r,c])
#             print(r, c)
    return matrixMovesList

            
# print(getMatrixMoves(getMoves(matrixSize)))

matrixMovesList = getMatrixMoves(getMoves(matrixSize))

# mainMatrix = []
# startRow = divmod(matrixSize, 2)[0]
# startCol = divmod(matrixSize, 2)[0]
# mainMatrix.append([startRow,startRow])
# mainMatrix = mainMatrix + matrixMovesList

mainMatrix = np.zeros((matrixSize,matrixSize))
# print(mainMatrix)

startRow = divmod(matrixSize, 2)[0]
startCol = divmod(matrixSize, 2)[0]
mainMatrix[(startRow,startCol)] = 1
currValue = 1
for li in matrixMovesList:
    mainMatrix[(li[0],li[1])] = currValue + 1
    currValue = currValue + 1
# print(mainMatrix)

# get the diagonal sum
diagSum = 0
for i in range(0,matrixSize):
    diagSum = diagSum + mainMatrix[i,i]
    diagSum = diagSum + mainMatrix[i,matrixSize-1-i]
diagSum = diagSum - mainMatrix[startRow,startCol]

print("The diagonals sum is: ", int(diagSum))
    
