'''
Created on Apr 27, 2020

@author: orcasweb
'''

powersDict = {}
for a in range(2,101):
    for b in range(2,101):
        p = pow(a,b)
        powersDict[p]=p
print(len(powersDict))
        