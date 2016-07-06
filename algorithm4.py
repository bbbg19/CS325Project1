
def linear(A)
    n = length(A)
    max_sum = -1
    ending_here_sum = -1
    for j in range(0, n-1)
        ending_here_high = j
        if ending_here_sum > 0
            ending_here_sum = ending_here_sum + A[j]
        else ending_here_low = j
            ending_here_sum = A[j]
        if ending_here_sum > max_sum
            max_sum =ending_here_sum
            low = ending_here_sum
            high = ending_here_high
    return {'max':max_sum, 'A': A[low:high]}
            
    
    