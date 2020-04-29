'''
Created on Apr 27, 2020

@author: orcasweb
'''

import itertools as itr

denominations = [100, 50, 20, 10, 5, 2, 1]
denomCombs = []
# # old code
# sumMain = 0
# combiCount = 0
# for i in range(1,len(denominations)+1):
#     lst = itr.combinations(denominations,i)
#     count = 0
#     for x in lst:
#         count = count + 1
#         denomCombs.append(x)
#     print(count)
#     sumMain = sumMain + count
# print("---")
# print(sumMain)
# print("---")
# print(denomCombs)

# a = 100, b = 50, c = 20, d = 10, e = 5, f = 2, g = 1
# Not including 200. I will add 1 

# we will see max times a number can occur to make 200
# 100  0<=a<=2
# 50  0<=b<=4
# 20  0<=c<=10
# 10  0<=d<=20
# 5   0<=e<=40
# 2   0<=f<=100
# 1   0<=g<=200

for a in range(3):
    cSum = (a * 100)
    if(cSum == 200):
        denomCombs.append([a])
        break
    elif(cSum > 200):
        break
    for b in range(5):
        cSum = (a * 100) + (b * 50)
        if(cSum == 200):
            denomCombs.append([a, b])
            break
        elif(cSum>200):
            break
        for c in range(11):
            cSum = (a * 100) + (b * 50) + (c * 20)
            if(cSum == 200):
                denomCombs.append([a, b, c])
                break
            elif(cSum > 200):
                break
            for d in range(21):
                cSum = (a * 100) + (b * 50) + (c * 20) + (d * 10)
                if(cSum == 200):
                    denomCombs.append([a, b, c, d])
                    break
                elif(cSum > 200):
                    break
                for e in range(41):
                    cSum = (a * 100) + (b * 50) + (c * 20) + (d * 10) + (e * 5)
                    if(cSum == 200):
                        denomCombs.append([a, b, c, d, e])
                        break
                    elif(cSum > 200):
                        break
                    for f in range(101):
                        cSum = (a * 100) + (b * 50) + (c * 20) + (d * 10) + (e * 5) + (f * 2)
                        if(cSum == 200):
                            denomCombs.append([a, b, c, d, e, d, f])
                            break
                        elif(cSum > 200):
                            break
                        for g in range(201):
                            cSum = (a * 100) + (b * 50) + (c * 20) + (d * 10) + (e * 5) + (f * 2) + (g * 1)
                            if(cSum == 200):
                                denomCombs.append([a, b, c, d, e, f, g])
                                break
                            elif(cSum > 200):
                                break
                            
filepath = r'..\resources\Problem_031.txt'
f = open(filepath, "w")
for comb in denomCombs:
    f.write('%s\n' % comb)
f.close()


print("The length of the combinations that make up 200 is:", len(denomCombs) + 1)
                            
