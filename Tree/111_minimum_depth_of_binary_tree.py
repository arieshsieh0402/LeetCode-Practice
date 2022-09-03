class Solution:
    # DFS
    def min_depth_dfs(self, root) -> int:
        if not root:
            return 0
        if not root.left or not root.right:
            return max(
                self.min_depth_dfs(root.left),
                self.min_depth_dfs(root.right)
            ) + 1
        else:
            return min(
                self.min_depth_dfs(root.left),
                self.min_depth_dfs(root.right)
            ) + 1
