# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursion
def postorder_traversal(root: Optional[TreeNode]) -> List[int]:
    traversal_post_order = []

    def dfs_post_order(node: Optional[TreeNode]) -> None:
        nonlocal traversal_post_order
        if not node:
            return

        dfs_post_order(node.left)
        dfs_post_order(node.right)
        traversal_post_order.append(node.val)

    dfs_post_order(root)
        
    return traversal_post_order



# Iteration
from collections import deque

def postorder_traversal(root: Optional[TreeNode]) -> List[int]:
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
    return traversal_post_order[::-1]

    
        
