#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
class MinStack:

    def __init__(self):
        self.stack = []
        self.minNum = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.minNum.append(val)
        if self.minNum[-1] >= val:
            self.minNum.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        tmp = self.stack.pop()
        if tmp == self.minNum[-1]:
            self.minNum.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minNum[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

