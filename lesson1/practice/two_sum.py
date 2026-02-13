# Problem 1
# Two Sum
# LeetCode 1
# https://leetcode.com/problems/two-sum/

class Solution:
	def twoSum(self, *args):
		pass

def run_tests():
	sol = Solution()
	print(sol.twoSum([2,7,11,15], 9))
	assert sol.twoSum([2,7,11,15], 9) == [0, 1]
	print(sol.twoSum([3,2,4], 6))
	assert sol.twoSum([3,2,4], 6) == [1, 2]

if __name__ == "__main__":
	run_tests()
