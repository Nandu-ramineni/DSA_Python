class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
class AVLTree:
    def __init__(self):
        self.root = None
    def height(self, node):
        if not node:
            return 0
        return node.height
    def balance(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)
    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        return x
    def rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        return y
    def insert(self, root, key):
        if not root:
            return AVLNode(key)
        if key < root.data:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)
        # LL
        if balance > 1 and key < root.left.data:
            return self.rotate_right(root)
        # RR
        if balance < -1 and key > root.right.data:
            return self.rotate_left(root)
        # LR
        if balance > 1 and key > root.left.data:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        # RL
        if balance < -1 and key < root.right.data:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)
        return root
    def preOrder_traversal(self, root):
        if root:
            print(root.data, end=' ')
            self.preOrder_traversal(root.left)
            self.preOrder_traversal(root.right)
    def inOrder_traversal(self,root):
        if root:
            self.inOrder_traversal(root.left)
            print(root.data, end=' ')
            self.inOrder_traversal(root.right)
    def postOrder_traversal(self,root):
        if root:
            self.postOrder_traversal(root.left)
            self.postOrder_traversal(root.right)
            print(root.data, end=' ')
    def minValueNode(self,Node):
        current = Node
        while current.left is not None:
            current = current.left
        return current
    def delete(self,root,key):
        if not root:
            return root
        if key < root.data:
            root.left = self.delete(root.left, key)
        elif key > root.data:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.minValueNode(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)
        if root is None:
            return root
        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)
        # LL    
        if balance > 1 and self.balance(root.left) >= 0:
            return self.rotate_right(root)
        # RR
        if balance < -1 and key > root.right.data:
            return self.rotate_left(root)
        # LR
        if balance > 1 and key > root.left.data:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        # RL
        if balance < -1 and key < root.right.data:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)
        return root    
avl = AVLTree()
root = None
keys = [15,13,4,3,6,21,18,5,9]
for key in keys:
    root = avl.insert(root, key)
print("PreOrder Traversal_AVL:")
avl.preOrder_traversal(root)
print("\nInOrder Traversal_AVL:")
avl.inOrder_traversal(root)
print("\nPostOrder Traversal_AVL:")
avl.postOrder_traversal(root)
dele=avl.delete(root,13)
print("\nPreOrder after delete:")
avl.preOrder_traversal(root)
print("\nInOrder after delete:")
avl.inOrder_traversal(root)
print("\nPostOrder after delete:")
avl.postOrder_traversal(root)


