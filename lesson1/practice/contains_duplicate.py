# Problem 2
# Contains Duplicate
# LeetCode 217
# https://leetcode.com/problems/contains-duplicate/

class Solution:
	def containsDuplicate(self, *args):
		pass

def run_tests():
	sol = Solution()
	print(sol.containsDuplicate([1,2,3,1]))
	assert sol.containsDuplicate([1,2,3,1]) == True
	print(sol.containsDuplicate([1,2,3,4]))
	assert sol.containsDuplicate([1,2,3,4]) == False

if __name__ == "__main__":
	run_tests()
