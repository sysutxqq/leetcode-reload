#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        indexOfs = {}  ## 存字符的下标
        maxLen = 0
        res = ''
        finalRes = ''
        ##一个字符一个字符的遍历
        for i in range(len(s)):
            ## 如果当前字符不在子串里
            if s[i] not in indexOfs.keys() or indexOfs[s[i]] < left:
                res = res + s[i]
                tmp = i - left + 1
                if tmp > maxLen:
                    maxLen = tmp
                    finalRes = res
            else:  ## 当前字符已经在子串里面了 从当前子串重新开始计算
                left = indexOfs[s[i]]
                res = s[i]
            indexOfs[s[i]] = i + 1
        return maxLen,finalRes

# @lc code=end
s = "pwwkew"
sol = Solution()
res,substr = sol.lengthOfLongestSubstring(s)
print(res,"  ",substr)
