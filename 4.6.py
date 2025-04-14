class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_same_tree(a: TreeNode, b: TreeNode) -> bool:

    if a is None and b is None:
        return True
    

    if a is None or b is None:
        return False
    

    if a.val != b.val:
        return False
    
    return is_same_tree(a.left, b.left) and is_same_tree(a.right, b.right)
