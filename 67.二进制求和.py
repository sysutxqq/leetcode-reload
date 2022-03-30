#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a)
        j = len(b)
        res = ''
        flag = False
        while(i > 0 and j > 0):
            tmp = int(a[i-1]) + int(b[j - 1]) + int(flag)
            if tmp == 2:
                res += str(0)
                flag = True
            elif tmp == 3:
                res += str(1)
                flag = True
            else:
                res += str(tmp)
                flag = False
            i -= 1
            j -= 1
        if i > 0:
            while(i > 0):
                tmp = int(a[i-1]) + int(flag)
                if tmp == 2:
                    res += str(0)
                    flag = True
                else:
                    flag = False
                    res += str(tmp)
                i -= 1
        if j > 0:
            while(j > 0):
                tmp = int(b[j-1]) + int(flag)
                if tmp == 2:
                    res += str(0)
                    flag = True
                else:
                    flag = False
                    res += str(tmp)
                j -= 1
        if flag:
            res += str(1)
        res = res[::-1]
        return res

# @lc code=end
sol = Solution()
a = "100"
b = "110010"
res = sol.addBinary(a,b)
