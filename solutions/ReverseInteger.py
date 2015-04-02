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
		current = n / 10**i
		n -= current * 10**i
		result += (current * 10**(total_digits-i))
		
	return result if positive else -result
	
	

def reverse2(self, x):
	x_str = str(x)
	magnitude = len(x_str)
	start = 1 if x < 0 else 0
	current_magnitude = 1
	result = 0
	
	for c in range(start, magnitude):
		result += int(x_str[c]) * current_magnitude
		current_magnitude *= 10
	
	if x < 0: 
		result *= -1
	
	return result
		
	
def test(exp, result):
	print("ok" if exp == result else "no - exp: {0} result: {1}".format(exp, result))
	

#test(123, reverse(None, 321))
test(-123, reverse(None, -321))
