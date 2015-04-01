def rob(self, num):
        
    houses = [0] + num + [0]*4
    
    current = 1
    
    robbedMoney = evenSum = oddSum = 0

    while(current <= len(num)+1):
        
        middle  = houses[current]
        right   = houses[current + 1]
        
        if middle + (evenSum if current % 2 == 0 else oddSum) > right + (oddSum if current % 2 == 0 else evenSum):
            robbedMoney += middle 
            robbedMoney += evenSum if current % 2 == 0 else oddSum
            evenSum = oddSum = 0
            current +=1
        elif current % 2 == 0:
            evenSum += middle
        else:
            oddSum += middle

        current +=1
        
    robbedMoney += max(evenSum, oddSum)
        
    return robbedMoney

def test(exp, real):
    if exp != real:
        print("{0} expected: {1} result: {2}".format(exp == real, exp, real))
    else: print("ok")

test(2, rob(None, [1,1,1]))
test(4, rob(None, [2,3,2]))
test(11, rob(None, [1,7,9,4]))
test(103, rob(None, [1,3,1,3,100]))
test(1082, rob(None, [82,217,170,215,153,55,185,55,185,232,69,131,130,102]))
test(27, rob(None, [6,6,4,8,4,3,3,10]))
test(19, rob(None, [2,4,8,9,9,3]))
test(42, rob(None, [1,1,3,6,7,10,7,1,8,5,9,1,4,4,3]))
test(4, rob(None, [2,1,1,2]))
# 217+215+185+232+131+102
#217+215+185+185+131+102

                