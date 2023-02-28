class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
       


class LinkedList:
    def __init__(self):
        self.head=None

    def add(self,data):
        new_node=node(data)
        new_node.next=self.head
        self.prev=new_node
        self.head=new_node

    def addinm(self,data,k):
        temp=self.head
        while temp:
            if temp.data==data:
                new_node=node(k)
                new_node.next=temp.next
                temp.next=new_node
                new_node.prev=temp
                temp.next.prev=new_node
                return
            temp=temp.next

    def printlist(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next

listed=LinkedList()
listed.add(100)
listed.add(50)
listed.add(12)
listed.addinm(50,60)
listed.addinm(60,600)

listed.printlist()
