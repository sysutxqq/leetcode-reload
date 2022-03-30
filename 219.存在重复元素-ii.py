#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#

# @lc code=start
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ## 试下用字典
        dict = {} ## 存数字和下标的映射
        for i in range(len(nums)):
            ## 如果词典中已经有这个数了，判断下标之间的距离
            if nums[i] in dict:
                if i - dict[nums[i]] <= k:
                    return True
            ## 否则 替代已经存在的映射关系
            dict[nums[i]] = i
        return False
                
# @lc code=end
sol = Solution()
nums = [1,0,1,1]
res = sol.containsNearbyDuplicate(nums,1)
