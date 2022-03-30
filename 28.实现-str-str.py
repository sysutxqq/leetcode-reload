#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ## solution 1 python index函数
        if needle not in haystack:
            return -1
        if len(needle) == 0:
            return 0
        res = haystack.index(needle)
        return res

        ## solution 2
        ## KMP算法 

# @lc code=end

