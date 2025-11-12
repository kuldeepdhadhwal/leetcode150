class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next
    def reverse_linked_list(self,head):
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        
        return prev
    


y = Node(5)
x = Node(10,y)
result = x.reverse_linked_list(x)
while result:
    print(result.value)
    result = result.next