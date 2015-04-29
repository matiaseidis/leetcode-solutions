# Reverse digits of an integer.
# Example1: x = 123, return 321
# Example2: x = -123, return -321

# @return an integer
def reverse(self, n):
	positive = n>=0
	total_digits = len(str(n))-1
	if not positive:
		total_digits -= 1
	n = abs(n)
	result = 0
	
	for i in range(total_digits, -1, -1):
		result += (n%10) * 10**i
		n = n / 10
		
	return result if positive else -result
	
def test(exp, result):
	print("ok" if exp == result else "no - exp: {0} result: {1}".format(exp, result))
	

#test(123, reverse(None, 321))
test(-123, reverse(None, -321))
