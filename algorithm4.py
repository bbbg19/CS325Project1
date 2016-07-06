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

A = [1, 4, -9, 8, 1, 3, 3, 1, -1, -4, -6, 2, 8, 19, -10, -11]
B = [2, 9, 8, 6, 5, -11, 9, -11, 7, 5, -1, -8, -3, 7, -2]
C = [10, -11, -1, -9, 33, -45, 23, 24, -1, -7, -8, 19]
D = [31,-41, 59, 26, -53, 58, 97, -93, -23, 84]
E = [3, 2, 1, 1, -8, 1, 1, 2, 3]
F = [12, 99, 99, -99, -27, 0, 0, 0, -3, 10]
G = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

resultA = linear(A)
resultB = linear(B)
resultC = linear(C)
resultD = linear(D)
resultE = linear(E)
resultF = linear(F) 
resultG = linear(G)

print resultA['maxSum']
print resultA['maxA']
print resultB['maxSum']
print resultB['maxA']
print resultC['maxSum']
print resultC['maxA']
print resultD['maxSum']
print resultD['maxA']
print resultE['maxSum']
print resultE['maxA']
print resultF['maxSum']
print resultF['maxA']
print resultG['maxSum']
print resultG['maxA']
            
    
    
