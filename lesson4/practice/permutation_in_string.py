# Problem 3
# Permutation in String
# LeetCode 567
# https://leetcode.com/problems/permutation-in-string/

class Solution:
	def checkInclusion(self, *args):
		pass

def run_tests():
	sol = Solution()
	print(sol.checkInclusion("ab", "eidbaooo"))
	assert sol.checkInclusion("ab", "eidbaooo") == True
	print(sol.checkInclusion("ab", "eidboaoo"))
	assert sol.checkInclusion("ab", "eidboaoo") == False

if __name__ == "__main__":
	run_tests()
