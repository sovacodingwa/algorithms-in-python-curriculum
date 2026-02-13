# Problem 2
# Search Insert Position
# LeetCode 35
# https://leetcode.com/problems/search-insert-position/

class Solution:
	def searchInsert(self, *args):
		pass

def run_tests():
	sol = Solution()
	print(sol.searchInsert([1,3,5,6], 5))
	assert sol.searchInsert([1,3,5,6], 5) == 2
	print(sol.searchInsert([1,3,5,6], 2))
	assert sol.searchInsert([1,3,5,6], 2) == 1

if __name__ == "__main__":
	run_tests()
