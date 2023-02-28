class node:
    def __init__(self,data):
        self.data=data
        self.next=None

one=node(5)
twoo=node(100)
three=node(20)

one.next=twoo
twoo.next=three
three.next=one

temp=one
while temp!=one:
    print(temp.data)
    temp=temp.next
