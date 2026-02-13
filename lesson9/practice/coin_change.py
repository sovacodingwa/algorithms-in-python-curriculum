# Problem 3
# Coin Change
# LeetCode 322
# https://leetcode.com/problems/coin-change/

class Solution:
	def coinChange(self, *args):
		pass

def run_tests():
	sol = Solution()
	print(sol.coinChange([1,2,5], 11))
	assert sol.coinChange([1,2,5], 11) == 3
	print(sol.coinChange([2], 3))
	assert sol.coinChange([2], 3) == -1

if __name__ == "__main__":
	run_tests()
