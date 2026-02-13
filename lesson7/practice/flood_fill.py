# Problem 3
# Flood Fill
# LeetCode 733
# https://leetcode.com/problems/flood-fill/

class Solution:
	def floodFill(self, *args):
		pass

def run_tests():
	sol = Solution()
	img = [[1,1,1],[1,1,0],[1,0,1]]
	print(sol.floodFill([row[:] for row in img], 1, 1, 2))
	assert sol.floodFill([row[:] for row in img], 1, 1, 2) == [[2,2,2],[2,2,0],[2,0,1]]

if __name__ == "__main__":
	run_tests()
