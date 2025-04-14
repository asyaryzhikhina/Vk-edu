class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def min_depth(root: TreeNode) -> int:
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    if root.left and root.right:
        return 1 + min(min_depth(root.left), min_depth(root.right))
    if root.left:
        return 1 + min_depth(root.left)
    if root.right:
        return 1 + min_depth(root.right)
