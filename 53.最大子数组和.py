#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#

# @lc code=start
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ## soluton 1 非动态规划
        ## 前面序列的和如果是负，那么在当前数值这里就直接重新开始一个序列
        ## 前面序列的和如果是正，那么对后面的求和是有好处的
        # preMax = nums[0]
        # subSum = 0
        # for i in range(len(nums)):
        #     if subSum < 0:
        #         subSum = nums[i]
        #     else:
        #         subSum += nums[i]
        #     preMax = max(subSum,preMax)
        # return preMax

        ## solution 2 动态规划
        ## 每一次与当前数字相加之后得到序列和，与当前值进行对比，取大的那个值作为当前子序列的最大和
        ## 将当前子序列最大和，与前面所有的序列最大和进行对比，取最大值
        preMax = 0
        resMax = nums[0]
        for i in range(len(nums)):
            sumList = preMax + nums[i]
            preMax = max(sumList,nums[i])
            resMax = max(preMax,resMax)
        return resMax
                
# @lc code=end
sol = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
res = sol.maxSubArray(nums)

