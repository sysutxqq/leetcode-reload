#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        ## 如果循环100次还没跳出循环，说明死循环了
        count = 100
        while(count > 0):
            if n == 1:
                return True
            else:
                tmp = self.isHappyHelper(n)
                n = tmp
            count -= 1
        return False
    
    ## 计算数字每个位置上的平方和
    def isHappyHelper(self,n:int) -> int:
        res = 0
        while(n > 0):
            remain = n%10
            res += remain * remain
            n = n//10
        return res
# @lc code=end

