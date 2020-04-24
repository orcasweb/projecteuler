'''
Created on Apr 20, 2020

@author: orcasweb
'''
from pandas.io.sas.sas_constants import rle_compression

'''
Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''
# import decimal
dLIMIT = 1000
NumRemainderDict = {}

# This is a custom method for this problem.
def myDivMod(numerator, denominator):
    nLen = len(str(numerator))
    dLen = len(str(denominator))
    lenDiff = dLen - nLen
        
    if(lenDiff > 0):
        numerator = numerator * (10 ** (lenDiff + 1))
    elif(lenDiff < 0):
        numerator = numerator * (10 ** (lenDiff + 1))
    elif(lenDiff == 0):
        if(numerator < denominator):
            numerator = numerator * (10 ** (lenDiff + 1))
        elif(numerator > denominator):
            pass
        elif(numerator == denominator):
            pass
    return divmod(numerator, denominator)


def getRemainderLength(denm):
    remDict = {}
    n = 1
    d = denm
    r = 0
    
    while(True):
        q, r = myDivMod(n, d)
        if(r != 0):
            n = r
#             print(q, r)
            if(r not in remDict.keys()):
                remDict[r]=r
            else:
                break
        else:
            break
    return len(remDict.keys())


# x = getRemainderLength(997)  
# print(x)  


    
for i in range(2,dLIMIT):
    rl = getRemainderLength(i)
    NumRemainderDict[i] = rl
    
# print(NumRemainderDict)
maxRem = max(NumRemainderDict.values())
dNum = None
print("The maximum length of the remainder(or repeating decimal) is: ",maxRem)
# print("The number ( d number below 1000) is: ",NumRemainderDict.items().)
for x in NumRemainderDict:
    if(NumRemainderDict[x]==maxRem):
        dNum = x
        print("The number ( d number below 1000) is: ",dNum)
        break
        
        
    
    
