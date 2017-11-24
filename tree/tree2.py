# --*-- coding:utf-8 --*--
class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def insert(self, root, node):
        if not root:
            root = node
        if root.data > node.data:
            if not root.left:
                root.left = node
            else:
                self.insert(root.left, node)
        else:
            if not root.right:
                root.right = node
            else:
                self.insert(root.right, node)


    def preOrder(self, node):
        if not node:
            return None
        print node.data
        left = self.preOrder(node.left)
        right = self.preOrder(node.right)


    def midOrder(self, node):
        if not node:
            return None
        left = self.midOrder(node.left)
        print node.data
        right = self.midOrder(node.right)


    def postOrder(self, node):
        if not node:
            return None

        left = self.postOrder(node.left)
        right = self.postOrder(node.right)
        print node.data

    def depth(self, node):
        if not node:
            return 0
        return self.depth(node.left) + 1 if self.depth(node.left) > self.depth(node.right) else self.depth(node.right) +1

    def getNlevelNodeNumbers(self, node, k):
        if not node or k < 1:
            return 0
        if k==1:
            return 1

        return self.getNlevelNodeNumbers(node.left, k-1) + self.getNlevelNodeNumbers(node.right, k-1)


    def isSameTree(self, node1, node2):
        if not node1 and not node2:
            return True
        elif node1 and node2:
            return node1.data == node2.data and self.isSameTree(node1.left, node2.left) and self.isSameTree(node1.right, node2.right)
        return False


    def mirror(self, node):
        if not node:
            return None
        tmp = node.left
        node.left = node.right
        node.right = tmp
        left = self.mirror(node.left)
        right = self.mirror(node.right)

    def leastCommonAncestor(self, node, target1, target2):
        if not node:
            return None
        if node is target1 or node is target2:
            return node

        left = self.leastCommonAncestor(node.left, target1, target2)
        right = self.leastCommonAncestor(node.right, target1, target2)

        if left and right:
            return node
        return left if left else right


    def distance(self, node, target):
        if not node:
            return -1
        if node is target:
            return 0
        dis = self.distance(node.left, target)
        if dis == -1:
            dis = self.distance(node.right, target)
        if dis != -1:
            return dis+1
        return -1

    def allAncestors(self, node, target):
        if not node:
            return False
        if node == target:
            return True
        if self.allAncestors(node.left, target) or self.allAncestors(node.right, target):
            print node.data
            return True
        return False

    def width(self, node, depth):
        if not node:
            return 0
        if depth == 1:
            return 1
        elif depth > 1:
            return self.width(node.left, depth-1) + self.width(node.right,depth-1)

    def maxWidth(self, node):
        maxWidth = 0
        depth = self.depth(node)
        for i in range(1, depth+1):
            width = self.width(node, i)
            if width > maxWidth:
                maxWidth = width
        return maxWidth

    def average(self, node):
        info = []
        def dfs(node, depth=0):
            if node:
                if len(info)<=depth:
                    info.append([0,0])
                info[depth][0] += node.data
                info[depth][1] += 1
                dfs(node.left, depth+1)
                dfs(node.right, depth+1)

        dfs(node)
        return [s/float(c) for s,c in info]

    def breadth_first_search(self, node):
        """
        广度优先遍历
        非递归 队列
        :param node:
        :return:
        """
        from collections import deque
        lst = deque()
        lst.append(node)
        while(lst):
            node = lst.popleft()
            print node.data
            if node.left:
                lst.append(node.left)
            if node.right:
                lst.append(node.right)


    def depth_first_search(self, node):
        """
        深度优先遍历
        非递归 栈
        :param node:
        :return:
        """
        from collections import deque

        lst = deque()
        lst.append(node)
        while(lst):
            node = lst.pop()
            print node.data
            if node.right:
                lst.append(node.right)
            if node.left:
                lst.append(node.left)


"""
            1
    2             3
4       5       6   [9]
"""
node = Node(1)
node.left = Node(2)
node.right = Node(3)
node.left.left = Node(4)
node.left.right = Node(5)
node.right.left = Node(6)


print 'pre'
print node.preOrder(node)
print '_______'

print 'mid'
print node.midOrder(node)
print '_______'

print 'post'
print node.postOrder(node)
print '_______'

node.insert(node, Node(9))

print 'pre'
print node.preOrder(node)
print '_______'

print 'mid'
print node.midOrder(node)
print '_______'

print 'post'
print node.postOrder(node)
print '_______'

print 'depth'
print node.depth(node)

print 'k level node number'
print node.getNlevelNodeNumbers(node, 3)

print 'is same tree'
import copy
node2 = copy.deepcopy(node)
node2.insert(node2, Node(10))
print node.isSameTree(node,node2)

print 'mirror'
'''
            1
    3             2
9       6      5     4
'''
node.mirror(node)
print node.preOrder(node)

print 'least common ancestor'
print node.getLeft().getLeft().data
print node.getLeft().getRight().getRight()
print node.leastCommonAncestor(node, node.getLeft().getLeft(), node.getLeft().getRight()).data

print 'distance'
target1 = node.getLeft().getLeft()
target2 = node.getLeft().getRight()
lca = node.leastCommonAncestor(node, target1, target2)
distance1 = node.distance(lca, target1)
distance2 = node.distance(lca, target2)
print distance1+distance2

print 'all ancestors'
node.allAncestors(node, node.getLeft().getLeft())

print 'max width'
print node.maxWidth(node)

print 'average'
print node.average(node)

print 'breadth first search'
node.breadth_first_search(node)

print 'depth first search'
node.depth_first_search(node)