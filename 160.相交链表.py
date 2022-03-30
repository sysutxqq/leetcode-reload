#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ## 遍历完A遍历B，遍历完B遍历A，最后两个链表的最后都是公共的部分
        p1 = headA
        p2 = headB
        ## 找跳出循环的条件，最后一个都为None
        while(p1 != p2):
            if p1 is None:
                p1 = headB
            else:
                p1 = p1.next
            
            if p2 is None:
                p2 = headA
            else:
                p2 = p2.next 
        return p1
        
# @lc code=end

