def deleteNode(node):
    if node is None:
        return
    curr_node = node.next
    node.data = curr_node.data
    node.next = curr_node.next


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        else:
            curr_node = self.head
            while curr_node.next is not None:
                curr_node = curr_node.next
            if curr_node.next is None:
                curr_node.next = Node(data)

    def toDeleteNode(self, value):
        curr_node = self.head
        while curr_node:
            if curr_node.data == value:
                break
            curr_node = curr_node.next
        if curr_node.data == value:
            return curr_node
        else:
            return None

    def display(self):
        if self.head is None:
            return "Non List"
        else:
            curr_node = self.head
            while curr_node:
                print(curr_node.data, end=" ")
                curr_node = curr_node.next


l = LinkList()
l.append(3)
l.append(4)
l.append(6)
l.append(9)
l.display()
node = l.toDeleteNode(9)
deleteNode(node)
print()
l.display()
