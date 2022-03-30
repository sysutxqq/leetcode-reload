#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ## 动态规划
        maxLen = 1
        res = ''
        dp = [[0 for i in range(len(s))] for j in range(len(s))]
        ##从最后开始遍历
        for left in range(len(s) - 1,-1,-1):
            ## 计算从left开始到最后一位中所有的子串是不是回文
            for right in range(left,len(s)):
                if left == right: ## 单个字符一定是回文串
                    dp[left][right] = 1
                elif left + 1 == right: ##相邻字符相等则一定是回文
                    if s[left] == s[right]:
                        dp[left][right] = 1
                else: ##如果left和right的字符相等 且中间的子串也是回文串，那也是回文
                    if s[left] == s[right] and dp[left + 1][right - 1] == 1:
                        dp[left][right] = 1
                ## 如果当前子串是回文串 看是不是最大回文串 
                if dp[left][right] == 1:
                    tmpStr = s[left:right + 1]
                    if len(tmpStr) >= maxLen:
                        res = tmpStr
                        maxLen = len(tmpStr)
        return res
# @lc code=end
sol = Solution()
s = "cbbd"
res = sol.longestPalindrome(s)

