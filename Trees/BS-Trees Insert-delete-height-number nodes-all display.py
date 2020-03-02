class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


l = Node(5)
l.right = Node(6)
l.left = Node(2)

