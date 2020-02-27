class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Trees:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            if data > self.root.data:
                if self.root.right is None:
                    self.root.right = Node(data)
                else:
                    self.root = self.root.right
            else:
                if self.root.left is None:
                    self.root.left = Node(data)
                else:
                    self.root = self.root.left
