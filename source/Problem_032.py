'''
Created on Apr 29, 2020

@author: orcasweb
'''
import timeit
start = timeit.default_timer()

# print(9999**0.5)
# print(99999**0.5)
# 99.99499987499375
# 316.226184874055


def isPandigital(i, j, k):
    isPan = False
    si = str(i)
    sj = str(j)
    sk = str(k)
    sijk = si + sj + sk
    
    if(len(str(sijk)) != 9):
        isPan = False
    else:
        pdList = [int(x) for x in str(sijk)]
        for i in range(1, 10):
            if(pdList.count(i) != 1):
                isPan = False
                break
            else:
                isPan = True
    return isPan

panProducts = {} 

'''

'''
for x in range(2,2000,):
    for y in range(2,2000):
        z = x * y
        if(isPandigital(x, y, z)):
                panProducts[z] = z
                print(x,y,z)



print(panProducts)
print("The sum of pan products is:" , sum(panProducts.values()))

stop = timeit.default_timer()
print('Time: ', stop - start) 
                
