# Recursion
def is_symmetric(root: Optional[TreeNode]) -> bool:
    if root == None:
            return True
        return is_symmetric_child_node(root.left, root.right)

def is_symmetric_child_node(left: [TreeNode], right: [TreeNode]) -> bool:
    if not left and not right:
        return True
    if not left or not right:
        return False
    return ((left.val == right.val) and
    (is_symmetric_child_node(left.left, right.right)) and
    (is_symmetric_child_node(left.right, right.left)))


# Stack
def is_symmetric(root: Optional[TreeNode]) -> bool:
    if root == None:
            return True
    stack = [(root.left, root.right)]

    while stack:
        left, right = stack.pop()
        if (
            (not left and not right) or
            (left and right and left.val == right.val)
        ):
            if left and right:
                stack.append((left.left, right.right))
                stack.append((left.right, right.left))
            continue
        else:
            return False
    return True
