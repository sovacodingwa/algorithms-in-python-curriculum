# Problem 2
# Contains Duplicate
# LeetCode 217
# https://leetcode.com/problems/contains-duplicate/

from typing import List

class Solution:
	def containsDuplicate(self, nums: List[int]) -> bool:
		pass

def run_tests():
	sol = Solution()
	print(sol.containsDuplicate([1,2,3,1]))
	assert sol.containsDuplicate([1,2,3,1]) == True
	print(sol.containsDuplicate([1,2,3,4]))
	assert sol.containsDuplicate([1,2,3,4]) == False

if __name__ == "__main__":
	run_tests()
