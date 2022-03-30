#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#

# @lc code=start
from cmath import inf
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ##找连续的子序列
        res = []
        index = 0
        startIndex = 0
        endIndex = 0
        #nums.append(-inf)  ## 在数字末尾加一个负无穷，就可以不用处理边界问题了
        while(index < len(nums)):
            ## 处理边界
            if index == len(nums) -1:
                if endIndex == startIndex:
                    subRes = str(nums[index])
                else:
                    subRes = str(nums[startIndex]) + '->' + str(nums[endIndex])
                res.append(subRes)
                break
            ##正常逻辑
            if nums[index + 1] == nums[index] + 1:
                endIndex += 1
            else:
                ## 子序列只有一个数
                if endIndex == startIndex:
                    subRes = str(nums[index])
                else:
                    subRes = str(nums[startIndex]) + '->' + str(nums[endIndex])
                res.append(subRes)
                startIndex = endIndex = index + 1
            index += 1
        return res
            

# @lc code=end

sol = Solution()
nums = [0,1,2,4,5,7]
res = sol.summaryRanges(nums)