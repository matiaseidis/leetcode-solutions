# Reverse bits of a given 32 bits unsigned integer.
# 
# For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), 
# return 964176192 (represented in binary as 00111001011110000010100101000000).

# @param n, an integer
# @return an integer
def reverseBits(self, n):
	result = ''
	for i in range(32):
		result += str(n & 1)
		n = n >> 1
		
	return int(result, 2)
	
		
def test(exp, result):
	if exp == result:
		print("ok")
	else: 
		print("no - exp: {0} result: {1}".format(exp, result))


print(str(test(964176192, reverseBits(None, 43261596))))


