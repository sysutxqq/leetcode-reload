#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        relation = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        num = 0
        i = 0
        ## 大的数字在前面，如果出现小的数字在前面就相减
        while(i < len(s) - 1):
            if relation[s[i]] >= relation[s[i+1]]:
                num = num + relation[s[i]]
                i += 1
            else:
                num = num + relation[s[i + 1]] - relation[s[i]]
                i += 2
        if i == len(s) - 1:
            num += relation[s[i]]
        return num

# @lc code=end
sol = Solution()
res = sol.romanToInt("LVIII")
