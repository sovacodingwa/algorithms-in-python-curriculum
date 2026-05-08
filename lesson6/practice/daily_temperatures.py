# Problem 3
# Daily Temperatures
# LeetCode 739
# https://leetcode.com/problems/daily-temperatures/

from typing import List

class Solution:
	def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
		pass

def run_tests():
	sol = Solution()
	print(sol.dailyTemperatures([73,74,75,71,69,72,76,73]))
	assert sol.dailyTemperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0]

if __name__ == "__main__":
	run_tests()
