# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        if(head ==None or head.next==None):
            return head
        head.val,head.next.val = head.next.val,head.val
        
        if head.next.next== None:
            return head
        self.swapPairs(head.next.next)
        
        return head
