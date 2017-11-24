"""
METHOD 1:
    recursively print each level.
    1: calculate the max height of the tree, height() method
    2: iterate each level and recursively decrease the level number
    and node go deeper in either left or right direction, level decreasing is negative direction,
    and tree traversing in positive direction

METHOD 2:
    use FIFO qeueu.
    1: add root to the FIFO queue
    2: pop the root and print it
    3: and push the root's left or right node in the queue if they exist
    4: in the while loop every time pop the 0 index of the queue, which is the level order when pushing into
    the queue from left child to right child, that's the level order.

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


#region METHOD 1
def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)

        return lheight+1 if lheight > rheight else rheight+1

def printLevelOrder(root):
    h = height(root)
    for i in range(1, h+1):
        printGivenLevel(root, i)

def printGivenLevel(root, level):
    if root is None:
        return
    elif level == 1:
        print ("%d" % root.data)
    else:
        printGivenLevel(root.left, level-1)
        printGivenLevel(root.right, level-1)

# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
#
# print (printLevelOrder(root))
#endregion ENDMETHOD 1

#region METHOD 2
def printLevelOrder(root):
    if root is None:
        return
    queue = []

    queue.append(root)
    while len(queue) > 0:
        node = queue.pop(0)
        print (node.data)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
printLevelOrder(root)


#endregion METHOD 2