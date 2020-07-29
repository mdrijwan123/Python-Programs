class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root):
        self.root = root

    def insert(self, root, data):
        if root is None:
            self.root = Node(data)
        else:
            if root.data < data:
                if root.right is None:
                    root.right = Node(data)
                else:
                    self.insert(root.right, data)
            elif data < root.data:
                if root.left is None:
                    root.left = Node(data)
                else:
                    self.insert(root.left, data)

    def display(self, root):
        if root is not None:
            self.display(root.left)
            print(root.data, end=" ")
            self.display(root.right)

    def search(self, root, data):
        if root is None:
            print("\nNot Found")
            return
        if root.data is data:
            print("\nFound")
            return
        if data > root.data:
            self.search(root.right, data)
        elif data < root.data:
            self.search(root.left, data)


if __name__ == "__main__":
    r = Node(5)
    t = Tree(r)
    t.insert(r, 6)
    t.insert(r, 3)
    t.insert(r, 3)
    t.insert(r, 7)
    t.display(r)
    t.search(r, 8)
