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
                maxA = A[:]
                
            
    return {'maxSum': maxSum, 'maxA': maxA}
               

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

outputFile.close()