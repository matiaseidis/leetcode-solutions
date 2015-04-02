# Reverse digits of an integer.
# Example1: x = 123, return 321
# Example2: x = -123, return -321

# @return an integer
def reverse(self, x):
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
	

test(123, reverse(None, 321))
test(-123, reverse(None, -321))
