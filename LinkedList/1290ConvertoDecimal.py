# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        prev = None
        curr = head

        while curr:
            temp_next = curr.next
            curr.next = prev
            prev = curr
            curr = temp_next
        res = 0
        count = 0
        while prev:
            if prev.val != 0:
                res += 2**count
            prev = prev.next
            count +=1
        return res