#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ## solution 1
        ## 取最短的字符串的长度
        ## 取出所有字符串挨个进行对比
        # subStr = ""
        # minLen = len(strs[0])
        # for s in strs:
        #     minLen = min(len(s),minLen)
        # flag = False
        # for i in range(minLen):
        #     common = strs[0][i]  ## 取出一个字符
        #     for s in strs:    ## 挨个字符串进行比较
        #         if s[i] != common:
        #             flag = True
        #             break
        #     if flag:
        #         return subStr
        #     else:
        #         subStr = subStr + common
        # return subStr

        ## solution 2
        ## 先对字符串进行排序，然后对比第一个和最后一个字符串的公共前缀
        strs.sort()  ## sort的时间复杂度 nlog(n)
        firstStr = strs[0]
        lastStr = strs[-1]
        l = min(len(firstStr),len(lastStr))
        res = ""
        for i in range(l):
            if firstStr[i] == lastStr[i]:
                res += firstStr[i]
            else:
                break
        return res

                
# @lc code=end

