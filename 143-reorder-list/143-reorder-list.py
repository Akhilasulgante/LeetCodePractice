# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        hare= tot = head
        #finding middle element
        while hare and hare.next:
            hare = hare.next.next
            tot = tot.next
            
        curr = tot
        prev = None
        
        #reversing the second half of linked list
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        #merging
        hare, tot = head, prev
        
        while tot.next:
            hare.next, hare = tot, hare.next
            tot.next, tot = hare, tot.next
        
            
            
            
            
        
        