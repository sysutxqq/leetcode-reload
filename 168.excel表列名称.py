#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ## solution 减1之后刚好是26进制
        ## A - Z的ascll码 = 65 ~ 90
        ## ord函数 -- > 输出字符的ascll码
        ## chr函数 -- > 输出ascll码的对应字符
        res = ''
        while(columnNumber > 0):
            tmp = (columnNumber - 1) % 26 ## 计算在26进制中的余数 
            subres = chr(65 + tmp)
            res += subres
            columnNumber = (columnNumber-1) // 26
        res = res[::-1]
        return res

# @lc code=end
sol = Solution()
res = sol.convertToTitle(701)
