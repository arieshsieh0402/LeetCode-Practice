from collections import deque


# Post_order
# Recursion
def recursive_post_order(node: Optional[TreeNode]) -> List[TreeNode]:
    traversal_order = []

    def dfs(node: Optional[TreeNode]):
        nonlocal traversal_order
        if not node:
            return

        dfs(node.left)
        dfs(node.right)
        traversal_order.append(node.val)

    dfs(node)

    return traversal_order


# Iteration
def iterative_post_order(node: Optional[TreeNode]) -> List[TreeNode]:
    traversal_order = deque()
    stack = []

    while stack or node:
        if node:
            stack.append(node)
            traversal_order.appendleft(node.val)  # reverse pre-order
            node = node.right  # reverse pre-order
        else:
            node = stack.pop()
            node = node.left  # reverse pre-order

    return list(traversal_order)


# Iteration without deque
def post_order_traversal_iter(root):
    traversal_post_order = []
    stack = [root]

    while stack:
        node = stack.pop()
        if node:
            traversal_post_order.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
    return traversal_post_order[::-1]


# Pre_order
# Recursion
def pre_order_traversal(root):
    traversal_pre_order = []

    def dfs_pre_order(node) -> None:
        nonlocal traversal_pre_order
        if not node:
            return
        traversal_pre_order.append(node.val)
        dfs_pre_order(node.left)
        dfs_pre_order(node.right)

    dfs_pre_order(root)

    return traversal_pre_order


# Iteration
def pre_order_traversal_iter(root):
    traversal_pre_order = []
    stack = [root]

    while stack:
        node = stack.pop()
        if node:
            traversal_pre_order.append(node.val)
            if node.right:
                stack.append(node.right)  # Coz stack LIFO
            if node.left:
                stack.append(node.left)
    return traversal_pre_order


# In_order
# Recursion
def recursive_in_order(node: Optional[TreeNode]) -> List[TreeNode]:
    traversal_order = []

    def dfs(node: Optional[TreeNode]):
        nonlocal traversal_order
        if not node:
            return

        dfs(node.left)
        traversal_order.append(node.val)
        dfs(node.right)

    dfs(node)

    return traversal_order


# Iteration
def recursive_in_order(node: Optional[TreeNode]) -> List[TreeNode]:
    traversal_order = []

    def dfs(node: Optional[TreeNode]):
        nonlocal traversal_order
        if not node:
            return

        dfs(node.left)
        traversal_order.append(node.val)
        dfs(node.right)

    dfs(node)

    return traversal_order
