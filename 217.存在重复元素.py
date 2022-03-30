#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#

# @lc code=start
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ## solution 1
        ## py in函数 超时
        # for i in range(len(nums)):
        #     if nums[i] in nums[i+1:]:
        #         return True
        # return False

        ## solution 2
        ## 用字典来做
        # dict = {}
        # for i in range(len(nums)):
        #     dict[nums[i]] = dict.get(nums[i],0) + 1
        # for k in dict.keys():
        #     if dict[k] >= 2:
        #         return True
        # return False

        ## soluton 3
        ## 用set来做
        tmpNums = set(nums)
        if len(tmpNums) < len(nums):
            return True
        return False
# @lc code=end
sol = Solution()

