def greedyCoin (denoms, inputValue):
    coins = []
    size = denoms.length - 1
    temp = inputValue
    count = 0
    
    while (temp > 0):
        if temp >= denoms[size]:
            temp = temp - denoms[size]
            coins[count] = denoms[size]
            count += 1
        else:
            size -= 1
    return coins