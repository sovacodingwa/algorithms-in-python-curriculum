# Problem 3
# Koko Eating Bananas
# LeetCode 875
# https://leetcode.com/problems/koko-eating-bananas/

class Solution:
	def minEatingSpeed(self, *args):
		pass

def run_tests():
	sol = Solution()
	print(sol.minEatingSpeed([3,6,7,11], 8))
	assert sol.minEatingSpeed([3,6,7,11], 8) == 4
	print(sol.minEatingSpeed([30,11,23,4,20], 5))
	assert sol.minEatingSpeed([30,11,23,4,20], 5) == 30

if __name__ == "__main__":
	run_tests()
