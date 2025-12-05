# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head

        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return head


###### Layman PsuedoCode ######################
'''
1. Here we have follow the two pointer approach
2. First we initialize both the pointer as flow and slow
3. For the first iteration the pointer will move to the n value which we use as a fast pointer
4. then we will add a condition if not fast, which means we don't get the fast than it will return head.next
5. Now we will do a while loop it doesnt reached at the end.
6. than slow.next = slow.next.next
7. The above line will simply remove the node and we will return the head

'''
