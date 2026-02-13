# Problem 1
# Max Area of Island
# LeetCode 695
# https://leetcode.com/problems/max-area-of-island/

class Solution:
	def maxAreaOfIsland(self, *args):
		pass

def run_tests():
	sol = Solution()
	grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
	print(sol.maxAreaOfIsland([row[:] for row in grid]))
	assert sol.maxAreaOfIsland([row[:] for row in grid]) == 6

if __name__ == "__main__":
	run_tests()
