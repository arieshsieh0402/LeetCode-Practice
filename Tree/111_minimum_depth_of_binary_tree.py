from collections import deque


def min_depth_dfs(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    if root.left and not root.right:
        return min_depth_dfs(root.left) + 1
    if root.right and not root.left:
        return min_depth_dfs(root.right) + 1

    return min(min_depth_dfs(root.left), min_depth_dfs(root.right)) + 1


def min_depth_bfs(root):
    if not root:
        return 0

    q = deque([(root, 1)])

    while q:
        curr_node, depth = q.popleft()
        if not curr_node.right and not curr_node.left:
            return depth
        if curr_node.left:
            q.append((curr_node.left, depth + 1))
        if curr_node.right:
            q.append((curr_node.right, depth + 1))
