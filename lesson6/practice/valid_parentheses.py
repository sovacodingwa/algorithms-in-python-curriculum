# Problem 1
# Valid Parentheses
# LeetCode 20
# https://leetcode.com/problems/valid-parentheses/

class Solution:
	def isValid(self, *args):
		pass

def run_tests():
	sol = Solution()
	print(sol.isValid("()"))
	assert sol.isValid("()") == True
	print(sol.isValid("(]"))
	assert sol.isValid("(]") == False

if __name__ == "__main__":
	run_tests()
