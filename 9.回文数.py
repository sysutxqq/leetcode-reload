#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start


class Solution:
    def isPalindrome(self, x: int) -> bool:
        ## soluton 1
        ## python list reverse()函数
        ## 转数组，需要注意的是，list的赋值是引用，需要使用[:]来进行赋值
        if x < 0:
            return False
        
        res = []
        while(x > 0):
            tmpNum = x % 10
            res.append(str(tmpNum))
            x = x // 10
        tmpRes = res[:]
        tmpRes.reverse()
        if res == tmpRes:
            return True
        return False


        ##不转字符串
# @lc code=end

