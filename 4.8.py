class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_mirror_twins(root: TreeNode) -> int:
    if not root:
        return 0
    
    def dfs(left, right):
        if not left or not right:
            return 0
        count = 0
        if left.val == right.val:
            count = 1
        count += dfs(left.left, right.right)
        count += dfs(left.right, right.left)
        return count
    
    return dfs(root.left, root.right)
