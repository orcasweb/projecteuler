'''
Created on Apr 27, 2020

@author: orcasweb
'''

'''
Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''

pwr5Dict = {}
pwr5Dict[0] = 0
pwr5Dict[1] = 1
pwr5Dict[2] = 32
pwr5Dict[3] = 243
pwr5Dict[4] = 1024
pwr5Dict[5] = 3125
pwr5Dict[6] = 7776
pwr5Dict[7] = 16807
pwr5Dict[8] = 32768
pwr5Dict[9] = 59049

resultsList = []
for x in range(1000,1000000):
    xSum = 0
    xList = [int(i) for i in str(x)]
    for xi in xList:
        xSum = xSum + pwr5Dict[xi]
    if(xSum==x):
        resultsList.append(x)
            
print(resultsList)
print(sum(resultsList))
            
            
            