# Problem 1
# Best Time to Buy and Sell Stock
# LeetCode 121
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
	def maxProfit(self, *args):
		pass

def run_tests():
	sol = Solution()
	print(sol.maxProfit([7,1,5,3,6,4]))
	assert sol.maxProfit([7,1,5,3,6,4]) == 5
	print(sol.maxProfit([7,6,4,3,1]))
	assert sol.maxProfit([7,6,4,3,1]) == 0

if __name__ == "__main__":
	run_tests()
