#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ## solution 1
        ## 首尾去掉空字符
        s = s.strip()
        tmp = s.split(' ')
        last = tmp[-1].strip()
        return len(last)
# @lc code=end
s = "   fly me   to   the moon  "
sol = Solution()
res = sol.lengthOfLastWord(s)

