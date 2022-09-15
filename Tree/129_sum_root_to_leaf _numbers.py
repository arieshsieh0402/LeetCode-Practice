def sum_numbers(root) -> int:
    def dfs(root, curr):
        if not root:
            return 0
        curr = curr * 10 + root.val
        if not root.left and not root.right:
            return curr
        return dfs(root.left, curr) + dfs(root.right, curr)
    return dfs(root, 0)
