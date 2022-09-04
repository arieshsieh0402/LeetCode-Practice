from collections import deque


# DFS-Recursion
def has_path_sum_dfs(root, target_sum: int) -> bool:
    if not root:
        return False
    if (
        not root.left and
        not root.right and
        root.val == target_sum
    ):
        return True
    return (
        has_path_sum_dfs(
            root.left, target_sum - root.val
        ) or
        has_path_sum_dfs(
            root.right, target_sum - root.val
        )
    )


# BFS-deque
def has_path_sum_bfs(root, target_sum: int) -> bool:
    if not root:
        return False

    q = deque([(root, target_sum - root.val)])

    while q:
        curr, val = q.popleft()
        if (
            not curr.left and
            not curr.right and
            val == 0
        ):
            return True
        if curr.left:
            q.append((curr.left, val - curr.left.val))
        if curr.right:
            q.append((curr.right, val - curr.right.val))
    return False
