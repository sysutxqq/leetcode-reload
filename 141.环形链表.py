#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ## solution 1
        ## 快慢指针，如果有环，则两个指针一定会相遇
        if head is None or head.next is None:
            return False

        # slow = head
        # fast = head
        # while(fast and fast.next):
        #     slow = slow.next
        #     fast = fast.next.next
        #     if slow == fast:
        #         return True
        # return False

        ## solution 2
        ## 赋一个特殊的值
        while(head):
            if head.val == 'txqqxx':
                return True
            else:
                head.val = 'txqqxx'
            head = head.next
        return False

# @lc code=end

