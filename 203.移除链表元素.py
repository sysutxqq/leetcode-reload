#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        newHead = ListNode()
        curNode = newHead
        node = head
        while(node):
            if node.val == val:
                node = node.next
                if node is None:
                    curNode.next = None
            else:
                curNode.next = node
                curNode = curNode.next
                node = node.next
        return newHead.next
# @lc code=end

