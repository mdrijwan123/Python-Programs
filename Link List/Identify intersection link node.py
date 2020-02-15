def intersetPoint(head_a, head_b):
    # code here
    h1 = head_a
    h2 = head_b
    d = {h1: 1}
    while h1 is not None:
        h1 = h1.next
        d[h1] = 1
    while h2 is not None:
        try:
            a = d[h2]
        except:
            b = 1
        else:
            ans = h2
            break
        h2 = h2.next
    return h2


# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        x, y, z = map(int, input().strip().split())
        a = LinkedList()  # create a new linked list 'a'.
        b = LinkedList()  # create a new linked list 'b'.
        nodes_a = list(map(int, input().strip().split()))
        nodes_b = list(map(int, input().strip().split()))
        nodes_common = list(map(int, input().strip().split()))

        for x in nodes_a:
            node = Node(x)
            a.append(node)  # add to the end of the list

        for x in nodes_b:
            node = Node(x)
            b.append(node)  # add to the end of the list

        for i in range(len(nodes_common)):
            node = Node(nodes_common[i])
            a.append(node)  # add to the end of the list a
            if i == 0:
                b.append(node)  # add to the end of the list b, only the intersection
        if intersetPoint(a.head, b.head) == -1:
            print(-1)
        else:
            print(intersetPoint(a.head, b.head).data)  # print data present at the node.
# } Driver Code Ends
