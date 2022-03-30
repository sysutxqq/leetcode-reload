#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

# @lc code=start
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ## solutio 1
        ## map实现，需要用额外的空间
        # count = {}
        # for i in range(len(nums)):
        #     count[nums[i]] = count.get(nums[i],0) + 1
        # for k in count:
        #     if count[k] == 1:
        #         return k


        ## solution 2
        ## 不使用额外的空间，位运算，异或
        ## 0和任意数异或等于任意数
        ## 异或运算满足交换律
        ## 相同两个数异或等于0
        res = 0
        for i in range(len(nums)):
            res = res^nums[i]
        return res


# @lc code=end

