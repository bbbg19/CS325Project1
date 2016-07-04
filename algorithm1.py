def enumeration(A):
    maxSum = A[0]
    for i in range(0, len(A)):
        newA = []
        newA.append(A[i])
        for j in range(i+1, len(A)):
            newA.append(A[j])
            if maxSum < sum(newA):
                maxSum = sum(newA)
    return maxSum
               

# A = [1, 4, -9, 8, 1, 3, 3, 1, -1, -4, -6, 2, 8, 19, -10, -11]               
# B = [2, 9, 8, 6, 5, -11, 9, -11, 7, 5, -1, -8, -3, 7, -2]
# C = [10, -11, -1, -9, 33, -45, 23, 24, -1, -7, -8, 19]
# D = [31,-41, 59, 26, -53, 58, 97, -93, -23, 84]
# E = [3, 2, 1, 1, -8, 1, 1, 2, 3]
# F = [12, 99, 99, -99, -27, 0, 0, 0, -3, 10]
# G = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# print enumeration(A)
# print enumeration(B)
# print enumeration(C)
# print enumeration(D)
# print enumeration(E)
# print enumeration(F)
# print enumeration(G)