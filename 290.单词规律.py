#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ## 
        s = s.split(' ') ## 先转换为列表
        if len(pattern) != len(s):
            return False
        relationSet = set()
        dict = {}
        for i in range(len(pattern)):
            if pattern[i] in dict:
                if s[i] not in relationSet:
                    return False
                elif dict[pattern[i]] != s[i]:
                    return False
            else:
                if s[i] in relationSet:
                    return False
            relationSet.add(s[i])
            dict[pattern[i]] = s[i]
        return True
# @lc code=end

