#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#

# @lc code=start


class Solution:
    def hammingWeight(self, n: int) -> int:
        ## solution
        ## 位运算 1的个数 = 模2的余数
        res = 0
        count = 32
        while(count > 0):
            if n % 2 == 1:
                res += 1
            n = n >> 1
            count -= 1
        return res
# @lc code=end

