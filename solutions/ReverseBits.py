# Reverse bits of a given 32 bits unsigned integer.
# 
# For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), 
# return 964176192 (represented in binary as 00111001011110000010100101000000).

# @param n, an integer
# @return an integer
	
def reverseBits(self, n):
	result = 0
	
	for i in range(31, -1, -1):
		result |= ((n & 1) << i)
		n = n >> 1
		
	return result

	
		
def test(exp, result):
	if exp == result:
		print("ok")
	else: 
		print("no - exp: {0} result: {1}".format(exp, result))


test(964176192, reverseBits(None, 43261596))


