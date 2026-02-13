# Problem 2
# Min Stack
# LeetCode 155
# https://leetcode.com/problems/min-stack/

class MinStack:
	def __init__(self):
		pass

	def push(self, val):
		pass

	def pop(self):
		pass

	def top(self):
		pass

	def getMin(self):
		pass

def run_tests():
	st = MinStack()
	st.push(-2)
	st.push(0)
	st.push(-3)
	print(st.getMin())
	assert st.getMin() == -3
	st.pop()
	print(st.top())
	assert st.top() == 0
	print(st.getMin())
	assert st.getMin() == -2

if __name__ == "__main__":
	run_tests()
