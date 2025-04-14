class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_subtree(A: TreeNode, B: TreeNode) -> bool:
    if B is None:
        return True
    if A is None:
        return False

    if is_same_tree(A, B):
        return True

    return is_subtree(A.left, B) or is_subtree(A.right, B)

def is_same_tree(a: TreeNode, b: TreeNode) -> bool:
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    return (a.val == b.val and 
            is_same_tree(a.left, b.left) and 
            is_same_tree(a.right, b.right))
