class Node:
    def __init__(self, dataval):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval


list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
i = 1
while i == 1:
    b = int(input("Enter the node to add in list\n"))
    c = Node(b)
    i = int(input("Entere the 1   for add one more node otherwise enter any number\n"))

# Link first Node to second node
list.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3

list.listprint()
