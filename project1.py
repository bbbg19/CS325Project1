import ast

def enumeration(A):
    if (len(A) == 1):
        maxSum = A[0]
        maxA = A
        return {'maxSum': maxSum, 'maxA': maxA}
    maxSum = A[0]
    maxA = []
    newA = []
    for i in range(0, len(A)):
        newA.append(A[i])
        for j in range(i+1, len(A)):
            newA.append(A[j])
            if maxSum < sum(newA):
                maxSum = sum(newA)
                maxA = newA[:]      #copy newA by val instead of ref
        newA = []
    return {'maxSum': maxSum, 'maxA': maxA}
    
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



#The linear implementation of max sub array
def linear(A):
    n = len(A)
    max_sum = -1
    ending_here_sum = -1
    low = 0 
    high = 0
    for j in range(0, n):
        ending_here_high = j
        if ending_here_sum > 0:
            ending_here_sum = ending_here_sum + A[j]
        else:
            ending_here_low = j
            ending_here_sum = A[j]
        if ending_here_sum > max_sum:
            max_sum = ending_here_sum
            low = ending_here_low
            high = ending_here_high
    maxA=A[low:high+1]
    
    return {'maxSum':max_sum, 'maxA': maxA}

#Recursive Solution
def mss(array, low, high):
	if(low == high):
		return array[low], low, high
		
 	mid = (low+high)/2
	
	#Get lower values
	leftValue, leftX, RightX = mss(array, low, mid)
	midValue, mleftX, mRightX = getCS(array, low, mid,high)
	rightValue, rLeftX, rRightX = mss(array, mid+1,high)
	
	if max(leftValue, midValue, rightValue) == leftValue:
		return leftValue, leftX, RightX
			
	elif max(leftValue, midValue, rightValue) == midValue:
		return midValue, mleftX, mRightX
		
	else:
		return rightValue, rLeftX, rRightX
		
	

	
 
#get crossing sum for recursive solution 
def getCS(array,low,mid, high):

	maxleft = -9999999
	maxright = -9999999
	maxLeftIndex =mid
	maxRightIndex =mid
	sum =0
	#get left sum
	for x in range(mid,low-1, -1):
		sum += array[x]
		if sum > maxleft:
			maxleft = sum
			maxLeftIndex =x
                      
	
	#get right sum 
	sum =0
	for x in range(mid+1,high+1):		
		sum += array[x]
		if (sum > maxright):
			maxright = sum	
			maxRightIndex = x
	return (maxleft + maxright), maxLeftIndex, maxRightIndex                

with open('MSS_Problems.txt', 'r') as ins:
    inputArrays = []
    for line in ins:
        inputArrays.append(ast.literal_eval(line))

outputFile = open('MSS_Results.txt', 'w')
outputFile.write("\nAlgorithm 1")
outputFile.write("**************************************\n")
for array in inputArrays:
    result = enumeration(array)
    outputFile.write(str(result['maxA']) + '\n' + str(result['maxSum']) + '\n')
outputFile.write("\nAlgorithm 2")
outputFile.write("**************************************\n")    
for array in inputArrays:
    result = betterEnumeration(array)
    outputFile.write(str(result['maxA']) + '\n' + str(result['maxSum']) + '\n')
outputFile.write("\nAlgorithm 3")
outputFile.write("**************************************\n")	
for array in inputArrays:
    result, left, right = mss(array,0, len(array)-1)
    outputFile.write(str(array[left:right+1]) + '\n' + str(result) + '\n')	
	
	
outputFile.write("\nAlgorithm 4")
outputFile.write("**************************************\n")    
for array in inputArrays:
    result = linear(array)
    outputFile.write(str(result['maxA']) + '\n' + str(result['maxSum']) + '\n')
outputFile.write("**************************************\n")
outputFile.close()