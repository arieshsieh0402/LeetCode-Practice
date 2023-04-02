from collections import deque
from typing import List, Optional


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    result = []
    q = deque([root])

    while q:
        new_level = []
        for _ in range(len(q)):
            node = q.popleft()
            new_level.append(node.val)
            for child in [node.left, node.right]:
                if child:
                    q.append(child)
        result.append(new_level)

    return result
