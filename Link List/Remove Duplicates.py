class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def insert(self,head,data):
            p = Node(data)
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        start = head
        while start.next is not None:
            after = start
            cnt = 0
            while after is not None and after.data == start.data:
                after = after.next
                cnt += 1
            if after is not None and after.data != start.data and cnt > 1:
                start.next = after
            if after is None and cnt > 1:
                start.next = None
                break
            start = start.next
        return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
head=mylist.removeDuplicates(head)
mylist.display(head)