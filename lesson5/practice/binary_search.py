# Problem 1
# Binary Search
# LeetCode 704
# https://leetcode.com/problems/binary-search/

from typing import List

class Solution:
	def search(self, nums: List[int], target: int) -> int:
		pass

def run_tests():
	sol = Solution()
	print(sol.search([-1,0,3,5,9,12], 9))
	assert sol.search([-1,0,3,5,9,12], 9) == 4
	print(sol.search([-1,0,3,5,9,12], 2))
	assert sol.search([-1,0,3,5,9,12], 2) == -1

if __name__ == "__main__":
	run_tests()
