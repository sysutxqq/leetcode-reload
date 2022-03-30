#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ## 计算数的次数，出现次数大于一半，那最后剩下的肯定是这个数
        count = 1
        majorNum = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == majorNum:
                count += 1
            else:
                count -= 1
            if count == 0:
                majorNum = nums[i]
                count = 1
        return majorNum
# @lc code=end
nums = [3,2,3]
sol = Solution()
res = sol.majorityElement(nums)

