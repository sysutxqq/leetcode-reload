#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ## solution 1
        ## 不改变数组，可以在数组内进行交换或者赋值，数组为有序数组，可以通过比较大小
        ## 来找到下一个需要的数字，下一次循环用这个数字与剩下的数字进行比较来移动两个指针
        ## 左右两个指针，一个记录左边的不重复数组长度，一个记录右边搜索到的需要加入的数字下标
        left = 1
        right = 1
        curNum = nums[0]  ## 记录当前用来比较的数字的大小
        while(right < len(nums)):
            if nums[right] <= curNum:
                right += 1
            else:
                nums[left] = nums[right]
                curNum = nums[right]
                left += 1
        return left
                
# @lc code=end
sol = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
res = sol.removeDuplicates(nums)

