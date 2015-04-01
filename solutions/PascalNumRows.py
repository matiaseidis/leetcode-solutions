



def generate(self, numRows):
    
    sol = [[1 for j in range(0, i)] for i in range(1, numRows+1)]
    
    for i in range(1, numRows):
        for j in range(1, i):
            sol[i][j] = sol[i-1][j-1] + sol[i-1][j]
        
    return sol
    
print(str(generate(None, 5)))