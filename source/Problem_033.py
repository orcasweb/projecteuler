'''
Created on Apr 30, 2020

@author: orcasweb
'''

'''
n1n2/d1d2  AND  n1,d1 not zero AND n1n2/d1d2 = n1/d1 or n1/d2 or n2/d1 or n2/d2 AND  n1n2/d1d2 < 1
find the four fractions, find their product , simplify and get the denominator
'''
import fractions as fr

frProduct = 1
def isDigitCancellingFraction(numerator, denominator):
    digitCancellingFraction = False
    nU = numerator % 10
    nT = int((numerator - nU) / 10)
    dU = denominator % 10
    dT = int((denominator - dU) / 10)
    if(nU == dU == 0):
        digitCancellingFraction = False
    elif((nT == dT) & (dU!=0)):
        if(numerator/denominator == nU/dU):
            digitCancellingFraction = True
    elif((nT == dU) & (dT!=0)):
        if(numerator/denominator == nU/dT):
            digitCancellingFraction = True
    elif((nU == dT) & (dU !=0)):
        if(numerator/denominator == nT/dU):
            digitCancellingFraction = True
    elif((nU == dU) & (dT !=0)):
        if(numerator/denominator == nT/dT):
            digitCancellingFraction = True

    return digitCancellingFraction


frList = []
# numerator will range from 10 to 98
for n in range(10, 99):
# denominator will range from one more than numerator to 99
    for d in range(n + 1, 100):
        if(isDigitCancellingFraction(n, d) == True):
            print(str(n) + '/' + str(d))
            frList.append(str(n) + '/' + str(d))
        
for frc in frList:
    frProduct = frProduct * fr.Fraction(frc)
print("The product of digit cancelling fractions is: ", frProduct)
print("The denominator is: ",fr.Fraction(frProduct).denominator)
    
