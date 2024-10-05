from typing import  List

# Define a tree node
class TreeNode:
    value: int
    children: List['TreeNode']

    def __init__(self, value: int) -> None:
        self.value = value
        self.children = []

    def add_child(self, node: 'TreeNode') -> None:
        self.children.append(node)

# Example usage
root = TreeNode(1)
child1 = TreeNode(2)
child2 = TreeNode(3)
root.add_child(child1)
root.add_child(child2)

print(root.value, [child.value for child in root.children])  # Output: 1 [2, 3]
