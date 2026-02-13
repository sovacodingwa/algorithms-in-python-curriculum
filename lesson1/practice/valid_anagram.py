# Problem 3
# Valid Anagram
# LeetCode 242
# https://leetcode.com/problems/valid-anagram/

class Solution:
	def isAnagram(self, *args):
		pass

def run_tests():
	sol = Solution()
	print(sol.isAnagram("anagram", "nagaram"))
	assert sol.isAnagram("anagram", "nagaram") == True
	print(sol.isAnagram("rat", "car"))
	assert sol.isAnagram("rat", "car") == False

if __name__ == "__main__":
	run_tests()
