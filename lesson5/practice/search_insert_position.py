# Problem 2
# Search Insert Position
# LeetCode 35
# https://leetcode.com/problems/search-insert-position/

from typing import List

class Solution:
	def searchInsert(self, nums: List[int], target: int) -> int:
		pass

def run_tests():
	sol = Solution()
	print(sol.searchInsert([1,3,5,6], 5))
	assert sol.searchInsert([1,3,5,6], 5) == 2
	print(sol.searchInsert([1,3,5,6], 2))
	assert sol.searchInsert([1,3,5,6], 2) == 1

if __name__ == "__main__":
	run_tests()
