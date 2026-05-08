# Problem 3
# Squares of a Sorted Array
# LeetCode 977
# https://leetcode.com/problems/squares-of-a-sorted-array/

from typing import List

class Solution:
	def sortedSquares(self, nums: List[int]) -> List[int]:
		pass

def run_tests():
	sol = Solution()
	print(sol.sortedSquares([-4,-1,0,3,10]))
	assert sol.sortedSquares([-4,-1,0,3,10]) == [0, 1, 9, 16, 100]

if __name__ == "__main__":
	run_tests()
