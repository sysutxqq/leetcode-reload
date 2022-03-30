#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        ## 翻转方向
        preNode = None  ## 新链表的尾部节点
        nextNode = head  ## 需要翻转的节点
        ## 割裂成两个部分
        while(nextNode):
            curNode = nextNode.next  ## 存后面还没有被改动的节点和节点关系
            nextNode.next = preNode
            preNode = nextNode
            nextNode = curNode
        return preNode
# @lc code=end
head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
sol = Solution()
res = sol.reverseList(head)


