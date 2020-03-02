class Node:
    def __init__(self,data):
        self.data = data
        self.left = left
        self.right = right

def insert(root,data):
    if root is None:
        root = Node(data)
    else:
        if data < root.data:
            