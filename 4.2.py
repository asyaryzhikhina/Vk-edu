from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_symmetric(root: TreeNode) -> bool:
    if not root:
        return True
    
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        for i in range(level_size // 2):
            left = queue[i]
            right = queue[level_size - 1 - i]
            
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
        
        for _ in range(level_size):
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)
    
    return True
