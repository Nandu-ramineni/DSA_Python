class TreeNode:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
        self.depth=0
def insert(root,value,depth):
        if not root:
            return TreeNode(value)
        if value < root.value:
            root.left=insert(root.left,value,depth+1)
        elif value >root.value:
            root.right=insert(root.right,value,depth+1)
        return root
def update_depths(root,depth):
        if root:
            root.depth=depth
            update_depths(root.left,depth+1)
            update_depths(root.right,depth+1)
def print_depth(root):
        if not root:
            return
        print(root.depth,end=' ')
        print_depth(root.left)
        print_depth(root.right)
def construct_bst(arr):
        root=None
        for value in arr:
            root=insert(root,value,0)
        update_depths(root,0)
        return root
def getHeight(root):
        if root is None:
            return -1
        left_height=getHeight(root.left)
        right_height=getHeight(root.right)
        return max(left_height,right_height)+1
n=7
nodes=[4,5,15,0,1,7,1]
bst_root=construct_bst(nodes)
print("print_depth:")
print_depth(bst_root)