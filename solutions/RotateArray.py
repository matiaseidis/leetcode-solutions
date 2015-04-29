#Rotate an array of n elements to the right by k steps.
#
#For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
#[1,2,3,4,5,6,7]
#[5,6,7,1,2,3,4]
#
#Note:
#Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

# @param nums, a list of integer
# @param k, num of steps
# @return nothing, please modify the nums list in-place.
def rotate(self, nums, k):
    N = len(nums)
    
  
            
    return nums

def next(current_index, step, total):
    candidate = current_index + step
    return candidate if candidate < total else candidate % total

def swap(nums, i, j):
    #print("swap for {0} and {1} in {2}".format(i, j, nums))
    current = nums[i]
    nums[i] = nums[j]
    nums[j] = current
    #print("after swap for {0} and {1} in {2}".format(i, j, nums))

def test(expected, real):
    if expected == real:
        print("ok")
    else: 
        print("expected {0} real {1}".format(expected, real))

test([5,6,7,1,2,3,4], rotate(None, [1,2,3,4,5,6,7], 3))