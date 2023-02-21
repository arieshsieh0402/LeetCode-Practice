from collections import deque


# recursively
def invert_tree(self, root):
    if root:
        root.left, root.right = (
            self.invert_tree(root.right), self.invert_tree(root.left)
        )
        return root


# BFS
def invert_tree_bfs(root):
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            node.left, node.right = node.right, node.left
            queue.append(node.left)
            queue.append(node.right)
    return root


# DFS
def invert_tree_dfs(root):
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            node.left, node.right = node.right, node.left
            stack.extend([node.right, node.left])
    return root
