from collections import deque


def min_depth_dfs(root):
    if not root:
        return 0
    if not root.left or not root.right:
        return max(
            min_depth_dfs(root.left),
            min_depth_dfs(root.right)
        ) + 1
    else:
        return min(
            min_depth_dfs(root.left),
            min_depth_dfs(root.right)
        ) + 1


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
