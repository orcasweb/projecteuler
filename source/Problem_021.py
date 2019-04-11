'''
Created on Apr 11, 2019

@author: orcasweb

'''
amicables = []
def getDivisorsN(n):
    divisors = []
    i = 1
    while(i<n):
        if(n%i == 0):
            divisors.append(i)
        i = i + 1
    return divisors
        
print(getDivisorsN(220)) # a = 220
print(sum(getDivisorsN(220))) # d(a) = d(220) = 284
print(getDivisorsN(sum(getDivisorsN(220)))) # b = 284
print(sum(getDivisorsN(sum(getDivisorsN(220))))) # d(b) = d(284) = 220    
        
n = 2
while(n<10000):
    a = n
    da = sum(getDivisorsN(n))
    b = da
    db = sum(getDivisorsN(b))
    if((a!=b)&(da==b)&(db==a)):
        amicables.append(a)
        amicables.append(b)
    n = n + 1
print(amicables)
print(set(amicables))
print("The sum of all the amicable numbers under 10000 is ",sum(set(amicables)))