'''
Created on Apr 10, 2019

@author: orcasweb
'''
# put the number of days in each month in reg year and leap year in a list
regYearMonthDays = [31,28,31,30,31,30,31,31,30,31,30,31]
leapYearMonthDays = [31,29,31,30,31,30,31,31,30,31,30,31]

# will use this to create a list of all days in a given month form 1901 to 2000
centList = []
# this is counter for months starting on Sundays
countSun = 0
# populate the centlist list
for x in range(1901,2001):
    if(x%4==0):
        centList = centList + leapYearMonthDays
    else:
        centList = centList + regYearMonthDays
print(centList)

# offset the sumDays becuase 1901 starts on tuesday and this results with week start on Sun
# this means the week beginning is always a sunday
sumDays = 2
for i in range(0,len(centList)):
#   add number of days in current month to running total and divide by 7.
#   whenever the remainder is 0 means that next month will start on Sunday.   
    sumDays = sumDays + centList[i]
    if(sumDays%7==0):
#       i is month in centlist List. 0 based so add 1 and divide by 12 to get years from 1901 
        year = 1901 + int((i+1)/12)
        month = 12 if(i+2)%12 == 0 else (i+2)%12
        print(i,year,month,sumDays/7,centList[i])
        countSun = countSun + 1
    
print(sumDays)
print("The number of months that start with Sunday:",countSun)        