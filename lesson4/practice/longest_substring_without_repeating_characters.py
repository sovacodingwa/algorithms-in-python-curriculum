# Problem 2
# Longest Substring Without Repeating Characters
# LeetCode 3
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
	def lengthOfLongestSubstring(self, *args):
		pass

def run_tests():
	sol = Solution()
	print(sol.lengthOfLongestSubstring("abcabcbb"))
	assert sol.lengthOfLongestSubstring("abcabcbb") == 3
	print(sol.lengthOfLongestSubstring("bbbbb"))
	assert sol.lengthOfLongestSubstring("bbbbb") == 1

if __name__ == "__main__":
	run_tests()
