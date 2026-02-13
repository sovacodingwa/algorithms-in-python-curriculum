# Problem 1
# Valid Palindrome
# LeetCode 125
# https://leetcode.com/problems/valid-palindrome/

class Solution:
	def isPalindrome(self, *args):
		pass

def run_tests():
	sol = Solution()
	print(sol.isPalindrome("A man, a plan, a canal: Panama"))
	assert sol.isPalindrome("A man, a plan, a canal: Panama") == True
	print(sol.isPalindrome("race a car"))
	assert sol.isPalindrome("race a car") == False

if __name__ == "__main__":
	run_tests()
