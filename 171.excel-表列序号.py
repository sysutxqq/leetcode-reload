#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel 表列序号
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ## 26进制
        res = 0
        for i in range(len(columnTitle)):
            tmp = ord(columnTitle[i]) - 65 + 1 ## 计算位上的数字
            res = res * 26 + tmp
        return res
# @lc code=end
sol = Solution()
res = sol.titleToNumber('ZY')

