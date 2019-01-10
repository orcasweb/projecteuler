'''
Created on Jan 9, 2019

@author: orcasweb
'''
# Largest palindrome product
# Problem 4
# 
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
# 
# Find the largest palindrome made from the product of two 3-digit numbers.

finalResult = -1
m = 999
n = 999
palinList = []

def isPalindrome(p):
    L = list(str(p))
    if(len(L) == 6):
        if((int(L[0]) == int(L[5])) & (int(L[1]) == int(L[4])) & (int(L[2]) == int(L[3]))):
            return True
        else:
            return False
    elif(len(L) == 5):
        if((int(L[0]) == int(L[4])) & (int(L[1]) == int(L[3]))):
            return True
        else:
            return False
    elif(len(L) == 4):
        if((int(L[0]) == int(L[3])) & (int(L[1]) == int(L[2]))):
            return True
        else:
            return False
    elif(len(L) == 3):
        if(int(L[0]) == int(L[2])):
            return True
        else:
            return False


# clumsy implementation
while(m > 99):
    while(n > 99):
        pr = m * n
#         print("The values are m=",m,"n=",n,"pr=",pr)
        if(isPalindrome(pr)):
            palinList.append(pr)
            print("The values are m=",m,"n=",n,"pr=",pr)
            break
        n = n - 1
    m = m - 1
    n = 999
print("the max palindrome is: ", max(palinList))



