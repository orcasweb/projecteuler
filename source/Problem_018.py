'''
Created on Apr 8, 2019

@author: orcasweb
'''


filePath = r'..\resources\Problem_018.txt'
lines = []
sumLines = []

f = open(filePath, 'r')
for l in f:
    lines.append(l.strip().split(" "))
    sumLines.append(l.strip().split(" "))
f.close()

depth = len(lines)

for i in range(0,depth):
    for j in range(0,len(lines[i])):
        lines[i][j] = int(lines[i][j])
        sumLines[i][j] = int(sumLines[i][j])
        

print(lines)
for m in range(depth-2,-1,-1):
    for n in range(0,len(lines[m])):
        sumLines[m][n] = max(sumLines[m][n] + sumLines[m+1][n], sumLines[m][n]+sumLines[m+1][n+1])
print(sumLines)
print("Max number is : ",sumLines[0][0])                                                     
         
         

         
       
 
 
         
     
