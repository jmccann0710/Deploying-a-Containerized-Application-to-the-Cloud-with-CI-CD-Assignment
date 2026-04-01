class Node:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None

def get_height(node):
  # TODO: write a recursive algorithm that returns
  # the height of the tree rooted at node.
  if node is None:
    return 0
  else:
    left_height = get_height(node.left)
    right_height = get_height(node.right)
    return 1 + max(left_height, right_height)

def get_depth(root, node):
  # TODO: write a recursive algorithm that returns
  # the depth of node in the tree rooted at root.
  if root is None or node is None:
    return -1

  if root == node:
    return 0

  left_depth = get_depth(root.left, node)
  right_depth = get_depth(root.right, node)

  if left_depth != -1:
    return 1 + left_depth
  elif right_depth != -1:
    return 1 + right_depth
  else:
    return -1

def get_node_count(root):
  # TODO: write a recursive algorithm that returns
  # the number of nodes in the tree rooted at root.
  return 0

def get_leaf_count(root):
  # TODO: write a recursive algorithm that returns
  # the number of leaves in the tree rooted at root.
  return 0

def is_full(root):
  # TODO: write a recursive algorithm that returns
  # True if the tree rooted at root is full, and
  # False, otherwise
  return False

def is_complete(root):
  # TODO: write a breadth-first traversal algorithm that returns
  # True if the tree rooted at root is complete, and False, otherwise
  return False




# -------------------------
# Create sample tree
# -------------------------
#        10
#       /  \
#      5    15
#     / \   /
#    2   7 12

root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)
root.right.left = Node(12)

assert get_height(root) == 2
assert get_height(root.left) == 1
assert get_height(root.left.left) == 0

assert get_depth(root, root) == 0
assert get_depth(root, root.left) == 1
assert get_depth(root, root.left.right) == 2
assert get_depth(root, root.right.left) == 2

assert get_node_count(root) == 6
assert get_node_count(root.left) == 3

assert get_leaf_count(root) == 3  # 2, 7, 12

assert is_full(root) == False  # node 15 has only one child

assert is_complete(root) == True  # last level filled left to right