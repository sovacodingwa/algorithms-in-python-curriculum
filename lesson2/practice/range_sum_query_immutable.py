# Problem 1
# Range Sum Query - Immutable
# LeetCode 303
# https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:
	def __init__(self, nums):
		pass

	def sumRange(self, left, right):
		pass

def run_tests():
	nums = [-2, 0, 3, -5, 2, -1]
	obj = NumArray(nums)
	print(obj.sumRange(0, 2))
	print(obj.sumRange(2, 5))
	print(obj.sumRange(0, 5))
	assert obj.sumRange(0, 2) == 1
	assert obj.sumRange(2, 5) == -1
	assert obj.sumRange(0, 5) == -3

if __name__ == "__main__":
	run_tests()
