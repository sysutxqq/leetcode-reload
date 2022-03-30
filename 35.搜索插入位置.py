#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
from platform import architecture
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ## solution 1 
        ## 找有序数组第一个大于等于该值的下标
        # for i in range(len(nums)):
        #     if nums[i] >= target:
        #         return i 
        # return len(nums)

        ## solution 2
        ## 用python的内置函数index
        # if target in nums:
        #     return nums.index(target)
        # for i in range(len(nums)):
        #     if target < nums[i]:
        #         return i
        # return len(nums)

        ## solution 3
        ## 直接加入list然后排序
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)



# @lc code=end
sol = Solution()
nums = [1,3,5,6]
res = sol.searchInsert(nums,2)