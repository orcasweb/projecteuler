'''
Created on Apr 19, 2020

@author: orcasweb
'''
print("In Fibonacci series that start with 1 and 1, the length of the number increases by 1 every five digits starting with seventh index")
print("F7 length is 2, \nF12 length is 3, \nF17 length is 4")


FibonacciSeries = [1,1]
LIMIT = 10000
for x in range(2,LIMIT+1):
    FibonacciSeries.append(FibonacciSeries[x-1] + FibonacciSeries[x-2])
    lenxPrev = len(str(FibonacciSeries[x-1]))
    lenx = len(str(FibonacciSeries[x]))
    if(lenx > lenxPrev):
        print("The index is: ",x+1, " and the length is: ",lenx)
        if(lenx == 1000):
            break

        
    
# indexNum = 7
# for len in range(3,1001):
#     indexNum = indexNum + 5
#     print("The index is: ",indexNum, " and the length is: ",len)

