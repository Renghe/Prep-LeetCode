from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        # Check if it's a leaf node and the sum matches
        if not root.left and not root.right:
            return targetSum == root.val

        # Recurse on left and right children
        return (self.hasPathSum(root.left, targetSum - root.val) or
                self.hasPathSum(root.right, targetSum - root.val))

# Helper to build binary tree from level-order list
def build_tree(values):
    if not values:
        return None
    from collections import deque
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

if __name__ == "__main__":
    tree_values = [5,4,8,11,None,13,4,7,2,None,None,None,1]
    target = 22

    root = build_tree(tree_values)
    sol = Solution()
    print(sol.hasPathSum(root, target))  # Output: True
