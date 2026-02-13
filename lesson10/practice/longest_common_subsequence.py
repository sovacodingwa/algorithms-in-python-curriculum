# Problem 3
# Longest Common Subsequence
# LeetCode 1143
# https://leetcode.com/problems/longest-common-subsequence/

class Solution:
	def longestCommonSubsequence(self, *args):
		pass

def run_tests():
	sol = Solution()
	print(sol.longestCommonSubsequence("abcde", "ace"))
	assert sol.longestCommonSubsequence("abcde", "ace") == 3

if __name__ == "__main__":
	run_tests()
