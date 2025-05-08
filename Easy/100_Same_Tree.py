from typing import Optional

# Define TreeNode class first
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Then define Solution class
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == "__main__":
    # Tree 1: [1, 2, 3]
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)

    # Tree 2: [1, 2, 3]
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)

    sol = Solution()
    print(sol.isSameTree(p, q))  # Output: True
