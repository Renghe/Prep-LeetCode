from typing import Optional, List

# Define the TreeNode structure
class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

# Recursive solution
class SolutionRecursive:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def traverse(node):
            if not node:
                return
            traverse(node.left)
            result.append(node.val)
            traverse(node.right)

        traverse(root)
        return result

# Iterative solution
class SolutionIterative:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result, stack = [], []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            result.append(current.val)
            current = current.right

        return result

# Helper function to build a binary tree from a list (level order)
def build_tree(values):
    if not values:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

# Sample test cases
if __name__ == "__main__":
    examples = [
        [1, None, 2, 3],
        [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9],
        [],
        [1]
    ]

    for idx, tree_data in enumerate(examples, 1):
        print(f"\nExample {idx}:")
        root = build_tree(tree_data)

        # Using Recursive
        recursive_result = SolutionRecursive().inorderTraversal(root)
        print(f"Recursive: {recursive_result}")

        # Using Iterative
        iterative_result = SolutionIterative().inorderTraversal(root)
        print(f"Iterative: {iterative_result}")
