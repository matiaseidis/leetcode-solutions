class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        
        result = ""
        for i in sorted(nums, cmp=Comp().lexicographic_comparator):
            result = result + str(i)
        return result if int(result) != 0 else "0"
        
class Comp:        
        
    def lexicographic_comparator(self, a_int,b_int):
        a = str(a_int)
        b = str(b_int)
        a_len = len(a)
        b_len = len(b)
        for i in range(0, max(a_len, b_len)):
            a_to_comp = a[0] if a_len <= i else a[i] 
            b_to_comp = b[0] if b_len <= i else b[i]
            if a_to_comp > b_to_comp:
                return -1
            elif a_to_comp < b_to_comp:
                return 1
        return 0 if a_len == b_len else -1 if a[a_len-1] > b[b_len-1] else 1 

def test(expected, result):
    if expected == result:
        print("ok")
    else:
        print("nop... |{0}| |{1}|".format(expected, result))

    
test("9534330", Solution().largestNumber([3, 30, 34, 5, 9]))
test("0", Solution().largestNumber([0,0]))
test("12121", Solution().largestNumber([121,12]))
