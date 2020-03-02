class Tree:
    def __init__(self,root):
        self.root = root
        self.left = None
        self.right = None
    def insert(self,data):
        if self.root:
            if data > self.root:
                if self.right is None:
                    self.right = Tree(data)
                else:
                    self.right.insert(data)
            elif data < self.root:
                if self.left is None:
                    self.left = Tree(data)
                else:
                    self.left.insert(data)
        else: self.root = data
    def display(self):
        if self.left:
            self.left.display()
        print(self.root)
        if self.right:
            self.right.display()

if __name__ == "__main__":
    t = Tree(5)
    t.insert(6)
    t.insert(7)
    t.insert(2)
    t.display()

        