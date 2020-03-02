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
                    self.right.insert(data)
            else:
                if self.root.left is None:
                    self.root.left = Node(data)
                else:
                    self.left.insert(data)

    def display(self):
        if self.root is None:
            return None
        if self.left
        self.left.display(self)
        print(self.root.data)
        self.right.display(self)

if __name__ == "__main__":
    t = Trees()
    t.insert(5)
    t.insert(7)
    t.insert(9)
    t.display()