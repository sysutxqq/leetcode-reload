#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#

# @lc code=start
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        ## solution 1
        ## 遍历一半进行前后交换
        # for i in range(len(s)//2):
        #     tmp = s[i]
        #     s[i] = s[len(s) - i - 1]
        #     s[len(s) - i - 1] = tmp

        ## solution 2
        ## 位运算来实现交换
        l = 0
        r = len(s) - 1
        while(l < r):
            s[l]^=s[r]
            s[r]^=s[l]
            s[l]^=s[r]
            l += 1
            r -= 1


        
# @lc code=end

