#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ## solution 动态规划
        res = []
        for i in range(0,numRows):
            subRes = [1] * (i + 1)    ## 先把每一行的base建起来
            for j in range(1,i):
                subRes[j] = res[i - 1][j - 1] + res[i - 1][j]
            res.append(subRes)
        return res

# @lc code=end

sol = Solution()
res =sol.generate(5)