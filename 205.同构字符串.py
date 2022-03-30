#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ## 注意不能多对一和一对多，用字典来做
        ## 长度不同直接返回false
        if len(s) != len(t):
            return False
        relationSet = set()  ## 存t中的值
        dict = {}
        for i in range(len(s)):
            if s[i] in dict: ## 如果x已经有了，那么看对应的y是不是也存在
                if t[i] not in relationSet: ## 如果对应的y不存在，说明存在一对多
                    return False
                else:
                    ##如果对应的y存在，看是不是满足映射关系
                    if dict[s[i]] != t[i]:
                        return False
            else:  ## 如果x还没有，看对应的y是不是存在
                if t[i] in relationSet: ## 如果对应的y已经在了，说明存在多对一
                    return False
                dict[s[i]] = t[i]
                relationSet.add(t[i])
        return True


# @lc code=end

