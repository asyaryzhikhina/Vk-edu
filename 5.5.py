class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.balance_factor = 0  

def calculate_heights_and_balance(node: TreeNode) -> int:
    if not node:
        return 0
    

    left_height = calculate_heights_and_balance(node.left)
    right_height = calculate_heights_and_balance(node.right)
    

    node.balance_factor = left_height - right_height

    return 1 + max(left_height, right_height)


def print_tree_info(node, level=0, prefix="Root: "):
    if node:
        print(" " * (level*4) + prefix + f"{node.val} (BF: {node.balance_factor})")
        print_tree_info(node.left, level+1, "L--- ")
        print_tree_info(node.right, level+1, "R--- ")
