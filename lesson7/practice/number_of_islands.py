# Problem 1
# Number of Islands
# LeetCode 200
# https://leetcode.com/problems/number-of-islands/

class Solution:
	def numIslands(self, *args):
		pass

def run_tests():
	sol = Solution()
	grid1 = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
	print(sol.numIslands([row[:] for row in grid1]))
	assert sol.numIslands([row[:] for row in grid1]) == 1

if __name__ == "__main__":
	run_tests()
