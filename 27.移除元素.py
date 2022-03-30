#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ## 左右两个指针
        ## 如果数值不在数组里 直接返回数组的长度，空数组也是
        if val not in nums:
            return len(nums)

        left = 0
        right = len(nums) - 1
        while(left < right):
            while(nums[left] != val and left < right):
                left += 1 
            while(nums[right] == val and left < right):
                right -= 1
            nums[left] = nums[right]
            nums[right] = val
        return left
            
# @lc code=end
sol = Solution()
nums = [2]
res = sol.removeElement(nums,3)