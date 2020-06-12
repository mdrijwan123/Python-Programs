class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root):
        self.root = Node(root)

    def print_inorder(self,traverse_type):
        if traverse_type == "inorder":
            return self.inorder_print(tree.root,"")

    def inorder_print(self, start,traverse):
        if start:
            traverse = self.inorder_print(start.left,traverse)
            traverse += (str(start.value) + "-")
            traverse = self.inorder_print(start.right,traverse)
        return traverse

tree = Tree(1)
tree.root.left = Node(5)
tree.root.right = Node(6)

print(tree.print_inorder("inorder"))
