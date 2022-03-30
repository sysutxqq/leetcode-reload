#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ## 考虑进位的情况，每位数都遍历的情况
        # flag = False
        # digits.reverse()
        # first = True
        # for i in range(len(digits)):
        #     if first:
        #         if digits[i] == 9:
        #             digits[i] = 0
        #             flag = True
        #         else:
        #             digits[i] = digits[i] + 1
        #         first = False
        #     else:
        #         if flag:
        #             if digits[i] == 9:
        #                 digits[i] = 0
        #                 flag = True
        #             else:
        #                 digits[i] = digits[i] + 1
        #                 flag = False

        # if flag:
        #     digits.append(1)
        # digits.reverse()
        # return digits

        ## 试试看只判断有进位的情况
        digits.reverse()
        flag = False
        if digits[0] == 9:
            digits[0] = 0
            flag = True
        else:
            digits[0] = digits[0] + 1
            digits.reverse()
            return digits

        i = 1
        while(flag and i < len(digits)):
            if digits[i] == 9:
                digits[i] = 0
                flag = True
            else:
                digits[i] = digits[i] + 1
                flag = False
            i += 1
        if flag:
            digits.append(1)
        digits.reverse()
        return digits

# @lc code=end
sol = Solution()
nums = [9,9]
res = sol.plusOne(nums)
