class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist:

    def __init__(self):
        self.head=None

    def insertNode(self,data):

        newNode = node(data)

        if self.head is None:
            self.head = newNode
            return
        else:
            last = self.head
            while last.next:
                last=last.next

            last.next=newNode
        return

    def printNode(self):
        count=0
        last=self.head
        while last:
            print(last.data)
            count+=1
            last=last.next
        print('c',count)


if __name__ == '__main__':
    a=linkedlist()
    a.insertNode(20)
    a.insertNode(30)
    a.insertNode(40)
    a.insertNode(200)
    a.insertNode(300)
    a.insertNode(11)
    a.insertNode(33)
    a.insertNode(99)
    a.insertNode(30)
    a.printNode()





