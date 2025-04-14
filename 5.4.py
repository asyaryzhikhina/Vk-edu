class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_min(node: TreeNode, k: int, counter: list) -> int:

    if not node:
        return None
    
    left_result = inorder_min(node.left, k, counter)
    if left_result is not None:
        return left_result

    counter[0] += 1
    if counter[0] == k:
        return node.val
    

    return inorder_min(node.right, k, counter)

def kth_smallest(root: TreeNode, k: int) -> int:
    counter = [0] 
    result = inorder_min(root, k, counter)
    if result is None:
        raise ValueError(f"Tree has fewer than {k} nodes")
    return result
