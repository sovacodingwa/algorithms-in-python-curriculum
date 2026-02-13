# Problem 2
# Subarray Sum Equals K
# LeetCode 560
# https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
	def subarraySum(self, *args):
		pass

def run_tests():
	sol = Solution()
	print(sol.subarraySum([1,1,1], 2))
	assert sol.subarraySum([1,1,1], 2) == 2
	print(sol.subarraySum([1,2,3], 3))
	assert sol.subarraySum([1,2,3], 3) == 2

if __name__ == "__main__":
	run_tests()
