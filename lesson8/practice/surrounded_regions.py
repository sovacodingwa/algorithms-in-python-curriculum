# Problem 2
# Surrounded Regions
# LeetCode 130
# https://leetcode.com/problems/surrounded-regions/

class Solution:
	def solve(self, *args):
		pass

def run_tests():
	board = [
		["X","X","X","X"],
		["X","O","O","X"],
		["X","X","O","X"],
		["X","O","X","X"],
	]
	Solution().solve(board)
	print(board)
	expect = [
		["X","X","X","X"],
		["X","X","X","X"],
		["X","X","X","X"],
		["X","O","X","X"],
	]
	assert board == expect

if __name__ == "__main__":
	run_tests()
