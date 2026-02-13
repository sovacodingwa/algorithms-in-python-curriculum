# Problem 3
# Word Search
# LeetCode 79
# https://leetcode.com/problems/word-search/

class Solution:
	def exist(self, *args):
		pass

def run_tests():
	sol = Solution()
	board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
	print(sol.exist([row[:] for row in board], "ABCCED"))
	assert sol.exist([row[:] for row in board], "ABCCED") == True

if __name__ == "__main__":
	run_tests()
