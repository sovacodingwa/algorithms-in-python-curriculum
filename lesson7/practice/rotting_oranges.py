# Problem 2
# Rotting Oranges
# LeetCode 994
# https://leetcode.com/problems/rotting-oranges/

class Solution:
	def orangesRotting(self, *args):
		pass

def run_tests():
	sol = Solution()
	grid1 = [[2,1,1],[1,1,0],[0,1,1]]
	print(sol.orangesRotting([row[:] for row in grid1]))
	assert sol.orangesRotting([row[:] for row in grid1]) == 4

if __name__ == "__main__":
	run_tests()
