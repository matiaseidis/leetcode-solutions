def hammingWeight(n):
    count = 0
    current = n
    while(current > 0):
        count += current % 2
        current /= 2
    return count
        
        
print(str(hammingWeight(10)))