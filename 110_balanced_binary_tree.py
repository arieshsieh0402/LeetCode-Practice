# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root) -> bool:
        if not root:
            return True

        def max_depth(root):
            if not root:
                return 0
            return max(max_depth(root.left), max_depth(root.right)) + 1

        if abs(max_depth(root.right) - max_depth(root.left)) <= 1:
            return self.isBalanced(root.right) and self.isBalanced(root.left)
        else:
            return False
