#Bitwise AND of Numbers Range  
#Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

#For example, given the range [5, 7], you should return 4.
from math import log

def rangeBitwiseAndAlternative(self, m, n):

    result = [False] * (int(log(n, 2))+1)
    while(m != 0):
        log_m = int(log(m, 2))
        if log_m != int(log(n, 2)):
            return parse(result)
        
        result[len(result)-log_m-1] = True
        to_handle = 2**log_m - 1
        m = m & to_handle
        n = n & to_handle
        
    return parse(result)

def parse(r):
    result = 0
    for bIdx in range(0, len(r)):
        if r[bIdx]:
            result = result | 2**(len(r)-bIdx-1)
    return result

def rangeBitwiseAnd(self, m, n):

    result = 0
    while(m != 0):
        log_m = int(log(m, 2))
        if log_m != int(log(n, 2)):
            return result
        
        to_handle = 2**log_m
        result = result | to_handle
        to_handle_minus_one = to_handle - 1
        m = m & to_handle_minus_one
        n = n & to_handle_minus_one
        
    return result

def test(expected, result):
    if expected == result:
        print("ok")
    else:
        print("expected {0} result {1}".format(expected, result)) 
        
test(12, rangeBitwiseAnd(None, 12,15))  
test(12, rangeBitwiseAnd(None, 13,15))  
test(4, rangeBitwiseAnd(None, 5,7))
#test(64, rangeBitwiseAnd(None, 83, 110)) # time out
#test(64, rangeBitwiseAnd(None, 0, 2147483647))


