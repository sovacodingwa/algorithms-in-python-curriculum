# Problem 3
# Find Pivot Index
# LeetCode 724
# https://leetcode.com/problems/find-pivot-index/

from typing import List

class Solution:
	def pivotIndex(self, nums: List[int]) -> int:
		pass

def run_tests():
	sol = Solution()
	print(sol.pivotIndex([1,7,3,6,5,6]))
	assert sol.pivotIndex([1,7,3,6,5,6]) == 3
	print(sol.pivotIndex([1,2,3]))
	assert sol.pivotIndex([1,2,3]) == -1

if __name__ == "__main__":
	run_tests()
