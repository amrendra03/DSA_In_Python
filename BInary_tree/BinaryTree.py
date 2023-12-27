class node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if self.data > data:
                if self.left is None:
                    self.left = node(data)
                else:
                    self.left.insert(data)
            elif self.data < data:
                if self.right is None:
                    self.right = node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data


def printt(root):
    lists = []
    return prints(root, lists)


# this coddde used to calculate the depth of node 31

def prints(root, lists):
    if root:
        prints(root.left, lists)
        prints(root.right, lists)
        if root.data == 31:
            return lists
        lists.append(root.data)
    return lists


def countLeaves(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    else:
        return countLeaves(root.left) + countLeaves(root.right)


root = node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
root.insert(100)

list = printt(root)
print(list)

'''
              27
           /      \
         14       35
        /   \    /   \
      10    19  31   42

in (Left -> Root -> Right)  = 10,14,19,27,31,35,42
pre(Root -> Left ->Right)   = 27,14,10,19,35,31,42
pos(Left ->Right -> Root)   = 10,19,14,31,42,35,27
'''
