import time
import random

def betterEnumeration(A):
    maxSum = 0
    maxA = []
    for i in range(0, len(A)):
        tempSum = 0
        for j in range(i, len(A)):
            tempSum += A[j]
            if maxSum < tempSum:
                maxSum = tempSum
                maxA = A[i:j+1]
                
            
    return {'maxSum': maxSum, 'maxA': maxA}
    
def generateArray(x):
	myList =[]
	for i in range(1,x):
		myList.append(random.randrange(-1000,1000))
		
	return myList
               

# A = [1, 4, -9, 8, 1, 3, 3, 1, -1, -4, -6, 2, 8, 19, -10, -11]               
# B = [2, 9, 8, 6, 5, -11, 9, -11, 7, 5, -1, -8, -3, 7, -2]
# C = [10, -11, -1, -9, 33, -45, 23, 24, -1, -7, -8, 19]
# D = [31,-41, 59, 26, -53, 58, 97, -93, -23, 84]
# E = [3, 2, 1, 1, -8, 1, 1, 2, 3]
# F = [12, 99, 99, -99, -27, 0, 0, 0, -3, 10]
# G = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# resultA = betterEnumeration(A)
# resultB = betterEnumeration(B)
# resultC = betterEnumeration(C)
# resultD = betterEnumeration(D)
# resultE = betterEnumeration(E)
# resultF = betterEnumeration(F) 
# resultG = betterEnumeration(G)

# print resultA['maxSum']
# print resultA['maxA']
# print resultB['maxSum']
# print resultB['maxA']
# print resultC['maxSum']
# print resultC['maxA']
# print resultD['maxSum']
# print resultD['maxA']
# print resultE['maxSum']
# print resultE['maxA']
# print resultF['maxSum']
# print resultF['maxA']
# print resultG['maxSum']
# print resultG['maxA']

outputFile = open('A2_times2.txt', 'w')
sizes = [11,51,101,501,1001,5001,10001,25001,50001]

for size in sizes:
	outputFile.write("Running sizes for " + str(size) + '\n')
	#run ten trials in this size
	for x in range (1,11):
		myList = generateArray(size)		
		start = time.clock()
		result = betterEnumeration(myList)
		end = time.clock()
# 		outputFile.write(str(result['maxA']) + '\n')
# 		outputFile.write(str(result['maxSum']) + '\n')
		outputFile.write("Trial Run " + str(x) + ". Time: " + str(end-start) + '\n')
	
outputFile.close()