#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#

# @lc code=start


class Solution:
    def reverseBits(self, n: int) -> int:
        ## solution 1
        ## 左移和右移
        ## 左移，左边丢弃，右边补0；右移，直接少一位；符号右边的数字表示要移动的位数
        ## 每一位都和1相与，结果左移再或下一次的相与结果，n进行右移

        ## 如果是带符号数
        ## 如果最右边一位是1，则表示是负数
        # if n&1 == 1:
        #     res = 1
        #     n = n >> 1
        # else:
        #     res = 0
        res = 0
        count = 32
        while(count > 0):  ## 终止循环
            tmp = n&1  ## 相与 取最后一位
            res = res << 1  ## 结果先左移一位
            res = res|tmp   ## 和最后一位进行或操作
            n = n >> 1   ## n进行右移，舍弃最后一位
            count -= 1   ## 计数-1
        return res
        
# @lc code=end

n = int('00000010100101000001111010011100',2)
sol = Solution()
res = sol.reverseBits(n)