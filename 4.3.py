class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_symmetric_dfs(root: TreeNode) -> bool:
    if not root:
        return True
    
    def depth_search(node, data):
        if not node:
            data.append(None)
            return
        data.append(node.val)
        depth_search(node.left, data)
        depth_search(node.right, data)
        return data
    
    data = depth_search(root, [])
    j = len(data) - 1
    
    for i in range(len(data) // 2):
        if data[i] != data[j]:
            return False
        j -= 1
    
    return True
