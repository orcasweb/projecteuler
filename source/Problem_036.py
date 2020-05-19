'''
Created on May 19, 2020

@author: orcasweb
'''
def isPalindrome(n):
    palindrome = False
    numList = [int(x) for x in str(n)]
    reverse_numList = numList[-1::-1]
    if(numList == reverse_numList):
        palindrome = True
    return palindrome

def isBinPalindrome(n):
    palindrome = False
    nBinStr = bin(n)[2:]
    nBinStr.lstrip('0')
    reverse_nBinStr = nBinStr[-1::-1]
    if(nBinStr == reverse_nBinStr):
        palindrome = True
    return palindrome



base10andbase2Palindomes = []

for num in range(1,1000000):
    if(isPalindrome(num) & isBinPalindrome(num)):
        base10andbase2Palindomes.append(num)

print(base10andbase2Palindomes)      
print("sum of base10 and base2 Palindomes below 1 million is: ", sum(base10andbase2Palindomes))

