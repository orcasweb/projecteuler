'''
Created on Apr 2, 2019

@author: orcasweb
'''
from math import log10
import time
'''


If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

'''
startTime = time.time()

numWordLookup = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven",
                 8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen",
                 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen",
                 20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty", 70:"seventy", 80:"eighty",
                 90:"ninety", 100:"hundred", 1000:"thousand" }

def getLength(num):
    return int(log10(num)) + 1


lim = 1000
finalString = ""
for x in range(1,lim+1):
    if(getLength(x)==1):
#         print(numWordLookup[x])
        finalString = finalString + numWordLookup[x]
    elif(getLength(x)==2):
        if(10<=x<=20):
#             print(numWordLookup[x])
            finalString = finalString + numWordLookup[x]
        else:
            tp = int(x/10)
            op = x - (tp*10)
            if(op == 0):
#                 print(numWordLookup[tp*10])
                finalString = finalString + numWordLookup[tp*10]
            else:
#                 print(numWordLookup[tp*10]+numWordLookup[op])
                finalString = finalString + numWordLookup[tp*10]+numWordLookup[op]
    elif(getLength(x)==3):
        hp = int(x/100) #get the hundredth's number
        tp = int((x - (hp*100))/10) #get the tens number
        op = x-((hp*100)+(tp*10))
#         print(hp,tp,op)
        if(((hp*100)+11)<=x<=((hp*100)+19)):
#             print(numWordLookup[hp]+"hundredand"+numWordLookup[tp*10+op])
            finalString = finalString + numWordLookup[hp]+"hundredand"+numWordLookup[tp*10+op]
        else:
            if(hp!=0 and tp==0 and op==0):
#                 print(numWordLookup[hp]+"hundred")
                finalString = finalString + numWordLookup[hp]+"hundred"
            elif(hp!=0 and tp==0 and op != 0):
#                 print(numWordLookup[hp]+"hundredand"+numWordLookup[op])
                finalString = finalString + numWordLookup[hp]+"hundredand"+numWordLookup[op]
            elif(hp!=0 and tp!=0 and op==0):
#                 print((numWordLookup[hp]+"hundredand"+numWordLookup[tp*10]))
                finalString = finalString + numWordLookup[hp]+"hundredand"+numWordLookup[tp*10]
            else:
#                 print((numWordLookup[hp]+"hundredand"+numWordLookup[tp*10])+numWordLookup[op])
                finalString = finalString + numWordLookup[hp]+"hundredand"+numWordLookup[tp*10]+numWordLookup[op]
            
    elif(getLength(x)==4):
#         print("onethousand")
        finalString = finalString + "onethousand"
print(finalString)
print(len(finalString))
endTime = time.time()
print("Finished in ",endTime-startTime)           
        
        
        
    
