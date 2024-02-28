class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return TreeNode(value)
    
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=" ")
        inorder_traversal(root.right)

def preorder_traversal(root):
    if root:
        print(root.value, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.value, end=" ")

def search(root, value):
    if root is None or root.value == value:
        return root
    
    if value < root.value:
        return search(root.left, value)
    else:
        return search(root.right, value)
        
def find_min_value(node):
    current = node
    while current.left is not None:
        current=current.left
    return current

def delete_node(root, value):
  if root is None:
    return root
  if value < root.value:
    root.left=delete_node(root.left, value)
  elif value>root.value:
    root.right=delete_node(root.right, value)
  else:
    if root.left is None:
      temp  = root.right
      root=None
      return temp
    elif root.right is None:
      temp=root.left
      root=None
      return temp
    else:
      if root.left.left is None and root.left.right is None and root.right.left is None and root.right.right is None:
        temp=find_min_value(root.left)
        root.value=temp.value
        root.left=delete_node(root.left, temp.value)
      else:
        temp=find_min_value(root.right)
        root.value=temp.value
        root.right=delete_node(root.right, temp.value)
    
  return root

if __name__ == "__main__":
    root = None
    values = [8,14,21,9,6,2,24]
    for value in values:
        root = insert(root, value)
    print("Inorder traversal:")
    inorder_traversal(root)
    print("\nPreorder traversal:")
    preorder_traversal(root)
    print("\nPostorder traversal:")
    postorder_traversal(root)
    print()
    value_to_delete = 6
    root = delete_node(root, value_to_delete)
    print("\nInordertraversal after del of node with value 6:")
    inorder_traversal(root)
    print("\npreordertraversal after del of node with value 6:")
    preorder_traversal(root)
    print("\npostordertraversal after del of node with value 6:")
    postorder_traversal(root)