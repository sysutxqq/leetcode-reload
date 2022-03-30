#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
        if n == 0:
            return nums1
        
        ## 从数组的尾巴开始填充，先判断两个数组最后的数字大小，大的放在nums1的最后
        while(m > 0 and n > 0):
            ## nums1中最后一个数比较大
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m = m - 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n = n - 1
        if n > 0:
            nums1[:n] = nums2[:n]
# @lc code=end
sol = Solution()
nums1 = [2,0]
nums2 = [1]
sol.merge(nums1,1,nums2,1)
