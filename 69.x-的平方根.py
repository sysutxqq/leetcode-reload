#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根 
#

# @lc code=start

class Solution:
    def mySqrt(self, x: int) -> int:
        ## solution 1 暴力
        # if x < 1:
        #     return 0
        
        # if x == 1:
        #     return 1
        # ## solution 1
        # for i in range(1,(x//2) + 1):
        #     if i*i <= x and (i+1)*(i+1) > x:
        #         return i
        
        ## solution 二分法
        if x == 0:
            return 0
        if x <= 2:
            return 1
        left = 0 
        right = (x//2) + 1
        while(right - left > 1): ## 如果精确到0.1 可以把区间值换成0.1
            mid = (left + right) // 2  ## 换成非整除
            if mid * mid > x:
                right = mid
            elif mid * mid < x:
                left = mid
            elif mid * mid == x:
                return mid
        return left
# @lc code=end
sol = Solution()
res = sol.mySqrt(8)

