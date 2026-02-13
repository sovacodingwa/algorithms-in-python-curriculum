# Problem 2
# Two Sum II - Input Array Is Sorted
# LeetCode 167
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
	def twoSum(self, *args):
		pass

def run_tests():
	sol = Solution()
	print(sol.twoSum([2,7,11,15], 9))
	assert sol.twoSum([2,7,11,15], 9) == [1, 2]
	print(sol.twoSum([2,3,4], 6))
	assert sol.twoSum([2,3,4], 6) == [1, 3]

if __name__ == "__main__":
	run_tests()
