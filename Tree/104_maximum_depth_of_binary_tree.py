from collections import deque


def max_depth(root):
    if not root:
        return 0
    return max(max_depth(root.left), max_depth(root.right)) + 1


def minDepth(root):
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
