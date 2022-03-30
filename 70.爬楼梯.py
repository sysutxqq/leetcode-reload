#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        ## solution 斐波拉契数列
        if n <= 2:
            return n
        f1 = 1
        f2 = 2
        if n >= 3:
            for i in range(2,n):
                tmp = f1 + f2
                f1 = f2
                f2 = tmp
        return f2

        ## solution 试一试递归 会超时
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        # if n >= 3:
        #     return self.climbStairs(n - 1) + self.climbStairs(n - 2)

# @lc code=end

sol = Solution()
res = sol.climbStairs(4)