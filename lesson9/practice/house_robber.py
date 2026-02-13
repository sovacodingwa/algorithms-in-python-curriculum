# Problem 2
# House Robber
# LeetCode 198
# https://leetcode.com/problems/house-robber/

class Solution:
	def rob(self, *args):
		pass

def run_tests():
	sol = Solution()
	print(sol.rob([1,2,3,1]))
	assert sol.rob([1,2,3,1]) == 4
	print(sol.rob([2,7,9,3,1]))
	assert sol.rob([2,7,9,3,1]) == 12

if __name__ == "__main__":
	run_tests()
