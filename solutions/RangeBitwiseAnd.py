
from math import log
def rangeBitwiseAnd(self, m, n):
        
        if n == m: 
            return m
        elif m == 0:
            return 0
        elif int(log(m, 2)) != int(log(n, 2)):
            return 0
        else:
            r = m
            while(log(m, 2) != log(n, 2)):
                r = r & m & n
                m = m << 1
                n = n >> 1
            return r
        
        

def test(a, b):
    if a == b:
        print("ok")
    else: 
        print(str(b))
    
test(32, rangeBitwiseAnd(None, 36, 54))
test(0, rangeBitwiseAnd(None, 4,22))
test(2, rangeBitwiseAnd(None, 2,3))
test(0, rangeBitwiseAnd(None, 1,5))
test(4, rangeBitwiseAnd(None, 5,7))
test(10, rangeBitwiseAnd(None, 10,10))
test(1, rangeBitwiseAnd(None, 1,1))
test(0, rangeBitwiseAnd(None, 0,1))
test(0, rangeBitwiseAnd(None, 2,11))

