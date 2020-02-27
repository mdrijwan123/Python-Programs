''' Read input from STDIN. Print your output to STDOUT '''


# Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    class Linked:
        def __init__(self):
            self.head = None

        def insert(self, data):
            if self.head is None:
                self.head = Node(data)
                return
            h = self.head
            while h.next is not None:
                h = h.next
            h.next = Node(data)

        def rem_odd(self):
            if self.head is None:
                return
            if self.head.next is None:
                self.head = None
            self.head = self.head.next
            h = self.head
            while h.next is not None:
                k = h.next
                h.next = k.next
                if h.next.next is not None:
                    h = h.next.next
                else:
                    h.next = None
                    break

        def display(self):
            if self.head is None:
                return
            h = self.head
            while h is not None:
                print(h.data)
                h = h.next

    l = Linked()
    n = int(input())
    for i in range(n):
        l.insert(int(input()))
    l.display()
    l.rem_odd()
    l.display()


main()
