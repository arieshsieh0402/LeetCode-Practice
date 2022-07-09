# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# =====PostOrder=====


# Recursion
def post_order_traversal(root: Optional[TreeNode]) -> List[int]:
    traversal_post_order = []

    def dfs_post_order(node: Optional[TreeNode]) -> None:
        nonlocal traversal_postorder
        if not node:
            return

        dfs_post_order(node.left)
        dfs_post_order(node.right)
        traversal_post_order.append(node.val)

    dfs_post_order(root)
        
    return traversal_post_order



# Iteration
from collections import deque

def post_order_traversal(root: Optional[TreeNode]) -> List[int]:
    traversal_post_order = deque()
    stack = [root]

    while stack:
        node = stack.pop()
        if node:
            traversal_post_order.appendleft(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
    return list(traversal_post_order)


# Iteration without deque
def postorder_traversal(root: Optional[TreeNode]) -> List[int]:
    traversal_post_order = []
    stack = [root]

    while stack:
        node = stack.pop()
        if node:
            traversal_post_order.appen(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
    return traversal_post_order[::-1]


# =====PreOrder=====

# Recursion
def pre_order_traversal(root: Optional[TreeNode]) -> List[int]:
    traversal_pre_order = []

    def dfs_pre_order(node: Optional[TreeNode]) -> None:
        nonlocal traversal_pre_order
        if not node:
            return
        traversal_pre_order.append(node.val)
        dfs_pre_order(node.left)
        dfs_pre_order(node.right)

    dfs_pre_order(root)

    return traversal_pre_order

# Iteration
def pre_order_traversal(root: Optional[TreeNode]) -> List[int]:
    traversal_pre_order = []
    stack = [root]

    while stack:
        node = stack.pop()
        if node:
            traversal_pre_order.append(node.val)
            if node.right:
                stack.append(node.right) # Coz stack LIFO 
            if node.left:
                stack.append(node.left)
    return traversal_pre_order


# =====InOrder=====

# Recursion
def in_order_traversal(root: Optional[TreeNode]) -> List[int]:
    traversal_in_order = []

    def dfs_in_order(node: Optional[TreeNode]) -> None:
        nonlocal traversal_in_order
        if not node:
            return
        dfs_in_order(node.left)
				traversal_in_order.append(node.val)
        dfs_in_order(node.right)

    dfs_in_order(root)

    return traversal_in_order


# Iteration
def in_order_traversal(root: Optional[TreeNode]) -> List[TreeNode]:
    traversal_in_order = []
    stack = []

    while stack or node:
        if node:
            stack.append(root)
            root = root.left
        else:
            node = stack.pop()
            traversal_in_order.append(node.val)
            node = node.right

    return traversal_in_order
