#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## 动态规划问题
        ## 记录最小的买入点，每往后一天就计算当天卖出的收益，与历史卖出的最大收益进行对比
        
        maxProfit = 0
        minBuyPoint = prices[0]
        for i in range(len(prices)):
            minBuyPoint = min(minBuyPoint,prices[i])
            tmpProfit = prices[i] - minBuyPoint
            maxProfit = max(tmpProfit,maxProfit)
        return maxProfit
        
# @lc code=end

