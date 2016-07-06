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

               

with open('MSS_Problems.txt', 'r') as ins:
    inputArrays = []
    for line in ins:
        inputArrays.append(ast.literal_eval(line))

outputFile = open('MSS_Results.txt', 'w')

for array in inputArrays:
    result = enumeration(array)
    outputFile.write(str(result['maxA']) + '\n' + str(result['maxSum']) + '\n')
    
for array in inputArrays:
    result = betterEnumeration(array)
    outputFile.write(str(result['maxA']) + '\n' + str(result['maxSum']) + '\n')
    
for array in inputArrays:
    result = linear(array)
    outputFile.write(str(result['maxA']) + '\n' + str(result['maxSum']) + '\n')

outputFile.close()