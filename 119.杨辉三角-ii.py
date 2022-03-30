#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = []
        for i in range(rowIndex + 1):
            subRes = [1] * (i + 1)
            for j in range(1,i):
                subRes[j] = res[i - 1][j - 1] + res[i - 1][j]
            res.append(subRes)
        return res[rowIndex]
# @lc code=end

