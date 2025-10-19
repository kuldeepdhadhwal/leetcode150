class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def insertNode(self, key):
        if self.val:
            if key < self.val:
                if self.left is None:
                    self.left = Node(key)
                else:
                    self.left.insertNode(key)
            elif key > self.val:
                if self.right is None:
                    self.right = Node(key)
                else:
                    self.right.insertNode(key)

    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.val)
            res = res + self.inorderTraversal(root.right)
        return res
    def preorderTraversal(self, root):
        res = []
        if root:
            res.append(root.val)
            res = res + self.preorderTraversal(root.left)
            res = res + self.preorderTraversal(root.right)

        return res
    def postorderTraversal(self,root):
        res = []
        if root:
            res = self.postorderTraversal(root.left)
            res = res + self.postorderTraversal(root.right)
            res.append(root.val)
        return res
    


n = Node(10)
n.insertNode(5)
n.insertNode(15)
n.insertNode(3)

print("Inorder Traversal:", n.inorderTraversal(n))
print("Preorder Traversal:", n.preorderTraversal(n))
print("Postorder Traversal:", n.postorderTraversal(n))

