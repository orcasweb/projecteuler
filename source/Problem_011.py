'''
Created on Jan 13, 2019

@author: orcasweb
'''

import pandas as pd
gridSize = 20
maxProd = 0



def getUp(x, y):
    upList = []
    if((0 < x - 3 < gridSize)):
        upList.append(int(df[x][y]))
        upList.append(int(df[x - 1][y]))
        upList.append(int(df[x - 2][y]))
        upList.append(int(df[x - 3][y]))
        return (upList[0] * upList[1] * upList[2] * upList[3])
    else:
        return -1


def getDown(x, y):
    downList = []
    if((0 < x + 3 < gridSize)):
        downList.append(int(df[x][y]))
        downList.append(int(df[x + 1][y]))
        downList.append(int(df[x + 2][y]))
        downList.append(int(df[x + 3][y]))
        return (downList[0] * downList[1] * downList[2] * downList[3])
    else:
        return -1


def getLeft(x, y):
    leftList = []
    if((0 < y - 3 < gridSize)):
        leftList.append(int(df[x][y]))
        leftList.append(int(df[x][y - 1]))
        leftList.append(int(df[x][y - 2]))
        leftList.append(int(df[x][y - 3]))
        return (leftList[0] * leftList[1] * leftList[2] * leftList[3])
    else:
        return -1


def getRight(x, y):
    rightList = []
    if((0 < y + 3 < gridSize)):
        rightList.append(int(df[x][y]))
        rightList.append(int(df[x][y + 1]))
        rightList.append(int(df[x][y + 2]))
        rightList.append(int(df[x][y + 3]))
        return (rightList[0] * rightList[1] * rightList[2] * rightList[3])
    else:
        return -1


def getDiagRightUp(x, y):
    diagRightUpList = []
    if((0 < x - 3 < gridSize) & (0 < y + 3 < gridSize)):
        diagRightUpList.append(int(df[x][y]))
        diagRightUpList.append(int(df[x - 1][y + 1]))
        diagRightUpList.append(int(df[x - 2][y + 2]))
        diagRightUpList.append(int(df[x - 3][y + 3]))
        return (diagRightUpList[0] * diagRightUpList[1] * diagRightUpList[2] * diagRightUpList[3])
    else:
        return -1


def getDiagRightDown(x, y):
    diagRightDownList = []
    if((0 < x + 3 < gridSize) & (0 < y + 3 < gridSize)):
        diagRightDownList.append(int(df[x][y]))
        diagRightDownList.append(int(df[x + 1][y + 1]))
        diagRightDownList.append(int(df[x + 2][y + 2]))
        diagRightDownList.append(int(df[x + 3][y + 3]))
        return (diagRightDownList[0] * diagRightDownList[1] * diagRightDownList[2] * diagRightDownList[3])
    else:
        return -1


def getDiagLeftUp(x, y):
    diagLeftUpList = []
    if((0 < x - 3 < gridSize) & (0 < y - 3 < gridSize)):
        diagLeftUpList.append(int(df[x][y]))
        diagLeftUpList.append(int(df[x - 1][y - 1]))
        diagLeftUpList.append(int(df[x - 2][y - 2]))
        diagLeftUpList.append(int(df[x - 3][y - 3]))
        return (diagLeftUpList[0] * diagLeftUpList[1] * diagLeftUpList[2] * diagLeftUpList[3])
    else:
        return -1


def getDiagLeftDown(x, y):
    diagLeftDownList = []
    if((0 < x - 3 < gridSize) & (0 < y + 3 < gridSize)):
        diagLeftDownList.append(int(df[x][y]))
        diagLeftDownList.append(int(df[x - 1][y + 1]))
        diagLeftDownList.append(int(df[x - 2][y + 2]))
        diagLeftDownList.append(int(df[x - 3][y + 3]))
        return (diagLeftDownList[0] * diagLeftDownList[1] * diagLeftDownList[2] * diagLeftDownList[3])
    else:
        return -1


df = pd.DataFrame([
['08', '02', '22', '97', '38', '15', '00', '40', '00', '75', '04', '05', '07', '78', '52', '12', '50', '77', '91', '08'],
['49', '49', '99', '40', '17', '81', '18', '57', '60', '87', '17', '40', '98', '43', '69', '48', '04', '56', '62', '00'],
['81', '49', '31', '73', '55', '79', '14', '29', '93', '71', '40', '67', '53', '88', '30', '03', '49', '13', '36', '65'],
['52', '70', '95', '23', '04', '60', '11', '42', '69', '24', '68', '56', '01', '32', '56', '71', '37', '02', '36', '91'],
['22', '31', '16', '71', '51', '67', '63', '89', '41', '92', '36', '54', '22', '40', '40', '28', '66', '33', '13', '80'],
['24', '47', '32', '60', '99', '03', '45', '02', '44', '75', '33', '53', '78', '36', '84', '20', '35', '17', '12', '50'],
['32', '98', '81', '28', '64', '23', '67', '10', '26', '38', '40', '67', '59', '54', '70', '66', '18', '38', '64', '70'],
['67', '26', '20', '68', '02', '62', '12', '20', '95', '63', '94', '39', '63', '08', '40', '91', '66', '49', '94', '21'],
['24', '55', '58', '05', '66', '73', '99', '26', '97', '17', '78', '78', '96', '83', '14', '88', '34', '89', '63', '72'],
['21', '36', '23', '09', '75', '00', '76', '44', '20', '45', '35', '14', '00', '61', '33', '97', '34', '31', '33', '95'],
['78', '17', '53', '28', '22', '75', '31', '67', '15', '94', '03', '80', '04', '62', '16', '14', '09', '53', '56', '92'],
['16', '39', '05', '42', '96', '35', '31', '47', '55', '58', '88', '24', '00', '17', '54', '24', '36', '29', '85', '57'],
['86', '56', '00', '48', '35', '71', '89', '07', '05', '44', '44', '37', '44', '60', '21', '58', '51', '54', '17', '58'],
['19', '80', '81', '68', '05', '94', '47', '69', '28', '73', '92', '13', '86', '52', '17', '77', '04', '89', '55', '40'],
['04', '52', '08', '83', '97', '35', '99', '16', '07', '97', '57', '32', '16', '26', '26', '79', '33', '27', '98', '66'],
['88', '36', '68', '87', '57', '62', '20', '72', '03', '46', '33', '67', '46', '55', '12', '32', '63', '93', '53', '69'],
['04', '42', '16', '73', '38', '25', '39', '11', '24', '94', '72', '18', '08', '46', '29', '32', '40', '62', '76', '36'],
['20', '69', '36', '41', '72', '30', '23', '88', '34', '62', '99', '69', '82', '67', '59', '85', '74', '04', '36', '16'],
['20', '73', '35', '29', '78', '31', '90', '01', '74', '31', '49', '71', '48', '86', '81', '16', '23', '57', '05', '54'],
['01', '70', '54', '71', '83', '51', '54', '69', '16', '92', '33', '48', '61', '43', '52', '01', '89', '19', '67', '48']])

for x in range(0, gridSize):
    for y in range(0, gridSize):
        print(df[x][y], end=' ')
        if(y == gridSize - 1):
            print()

for x in range(0, gridSize):
    for y in range(0, gridSize):
        print('[', format(x, '02d'), '][', format(y, '02d'), ']', end=' ', sep='')
        if(y == gridSize - 1):
            print()

for x in range(0, gridSize):
    for y in range(0, gridSize):
        val = getUp(x, y)
        if(val > maxProd):
            maxProd = val 
            print(x, y, "getUp", maxProd)
        
        val = getDown(x, y)
        if(val > maxProd):
            maxProd = val 
            print(x, y, "getDown", maxProd)

        val = getLeft(x, y)
        if(val > maxProd):
            maxProd = val 
            print(x, y, "getLeft", maxProd)

        val = getRight(x, y)
        if(val > maxProd):
            maxProd = val 
            print(x, y, "getRight", maxProd)
            
        val = getDiagRightUp(x, y)
        if(val > maxProd):
            maxProd = val 
            print(x, y, "getDiagRightUp", maxProd)

        val = getDiagRightDown(x, y)
        if(val > maxProd):
            maxProd = val 
            print(x, y, "getDiagRightDown", maxProd)

        val = getDiagLeftUp(x, y)
        if(val > maxProd):
            maxProd = val 
            print(x, y, "getDiagLeftUp", maxProd)

        val = getDiagLeftDown(x, y)
        if(val > maxProd):
            maxProd = val 
            print(x, y, "getDiagLeftDown", maxProd)
