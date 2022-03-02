#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ##solution 1
        ##python list的index函数
        ##index函数可以指定查找的范围，nums.index(num,start,end)
        ##index的时间复杂度o(n),算法实现起来时间复杂度还是o(n^2)
        ##python内置函数时间负责度：https://wiki.python.org/moin/TimeComplexity

        # res = []
        # for i in range(len(nums)):
        #     tmpNum = target - nums[i]
        #     if tmpNum in nums[i+1:]:
        #          res.append(i)
        #          res.append(nums.index(target - nums[i],i+1))
        #          break
        # return res

        ##solution 2
        ##用map做，map in操作的平均时间复杂度为o(1)
        numMap = {}
        for index,val in enumerate(nums):
            tmpNum = target - val  # 找另外一个数
            if tmpNum in numMap.keys():  #如果在map中，就直接返回
                return [index,numMap[tmpNum]]
            else:
                numMap[val] = index  #不在就加入map
        return None
        

# @lc code=end

