#
# @lc app=leetcode.cn id=258 lang=python3
#
# [258] 各位相加
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        ##举个例子
        ## 百位：x，十位：y，个位：z
        ## num = 100x + 10y +z = 99x + 9y +(x+y+z)
        ## 我们要找的就是x+y+z，也就是num % 9的值，需要考虑x+y+z=9的情况，是需要返回9的
        if num == 0:
            return 0
        res =  num % 9
        if res == 0:
            return 9

        return res
# @lc code=end

