'''
Created on Jan 11, 2019

@author: orcasweb
'''
abcMax = 1000
aMax = int(abcMax / 2) - 1  # 499
bMax = int(abcMax / 2) + 1  # 501
a = 1
b = 2
c = 3
for a in range(1, aMax + 1):
    for b in range(a + 1, bMax + 1):
        c = int(abs((a ** 2 + b ** 2) ** 0.5))
        if((a + b + c) == abcMax):
            # print(a, b, c)
            if((a ** 2 + b ** 2) == (c ** 2)):
                print(a, b, c)
                print(a**2 + b**2, c**2)
                print(a*b*c)


