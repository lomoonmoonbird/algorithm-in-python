
class Node():
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None



class BST():
    def __init__(self):
        self.root = None


    def insert(self, node, data):
        new = Node(data)
        if not self.root:
            self.root = node

        if data > node.data:
            if not node.right:
                node.right = new
            else:
                self.insert(node.right, data)

        if data < node.data:
            if not node.left:
                node.left = new
            else:
                self.insert(node.left, data)

        else:
            return None
        return new


b = BST()
b.insert(None, 1)
print b