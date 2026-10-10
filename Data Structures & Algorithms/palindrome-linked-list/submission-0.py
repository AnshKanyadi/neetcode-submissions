# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        end = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            end = end.next

        prev = None 
        while end:
            nextnode = end.next
            end.next = prev
            prev = end
            end = nextnode
        

        while head and prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        

        return True
        
       
        



        
        


        