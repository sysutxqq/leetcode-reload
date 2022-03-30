#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2 的幂
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        ## solution 1
        ## 不断模2 如果有余数就说明不是
        # while(n > 0):
        #     if n == 1:
        #         return True
        #     if n%2 == 1:
        #         return False
        #     n = n // 2
        # return False

        ## solution 2
        ## 位运算，和n-1 相互与一定是等于0
        if n == 0:
            return False
        if n & (n-1) == 0:
            return True
        return False
# @lc code=end

