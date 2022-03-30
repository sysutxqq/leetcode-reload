#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start

class Solution:
    def isValid(self, s: str) -> bool:
        ## solution 1 
        ## 用栈的思维来做
        # stack = []
        # for i in range(len(s)):
        #     if s[i] == '(' or s[i] == '[' or s[i] == '{':
        #         stack.append(s[i])
        #     elif s[i] == ')':
        #         if len(stack) == 0:
        #             return False
        #         tmp = stack[-1]
        #         if tmp == '(':
        #             stack.pop()
        #         else:
        #             return False
        #     elif s[i] == ']':
        #         if len(stack) == 0:
        #             return False
        #         tmp = stack[-1]
        #         if tmp == '[':
        #             stack.pop()
        #         else:
        #             return False
        #     elif s[i] == '}':
        #         if len(stack) == 0:
        #             return False
        #         tmp = stack[-1]
        #         if tmp == '{':
        #             stack.pop()
        #         else:
        #             return False
        # if stack:
        #     return False
        # return True

        ## solution 2
        ## python 替换 replace,该函数是有返回值的
        while('()' in s or '[]' in s or '{}' in s):
            s = s.replace('{}','')
            s = s.replace('()','')
            s = s.replace('[]','')
        return len(s)==0
# @lc code=end
sol = Solution()
s = "()[]{}"
res = sol.isValid(s)