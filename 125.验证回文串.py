#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # solution 1
        # python 去掉字符串中的符号和空格
        # subStr = []
        # for i in s:
        #     if i.isalnum():
        #         subStr.append(i.lower()) 
        # tmp = subStr[:]
        # tmp.reverse()
        # if tmp == subStr:
        #     return True
        # return False

        ## solution 2
        ## filter 函数
        subStr = ''.join(filter(str.isalnum,s)).lower()
        return subStr == subStr[::-1]
# @lc code=end
s = "A man, a plan, a canal: Panama"
sol = Solution()
res = sol.isPalindrome(s)

