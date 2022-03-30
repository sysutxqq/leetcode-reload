#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        ## solution 1 
        ## 借用一个set来存值
        # newHead = ListNode()
        # curNode = newHead
        # valSet = set()
        # while(head):
        #     if head.val in valSet:
        #         head = head.next
        #         if head is None:
        #             curNode.next = None
        #     else:
        #         curNode.next = head
        #         valSet.add(head.val)
        #         head = head.next
        #         curNode = curNode.next
        # return newHead.next

        ## solution 2
        ## 利用有序链表
        if head is None:
            return None
        curNode = head
        while(curNode.next):
            if curNode.val == curNode.next.val:
                curNode.next = curNode.next.next
            else:
                curNode = curNode.next
        return head
# @lc code=end
head = ListNode(1,ListNode(1,ListNode(2,ListNode(3,ListNode(3)))))
sol = Solution()
res = sol.deleteDuplicates(head)