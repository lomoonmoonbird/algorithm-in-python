# --*-- coding: utf-8 --*--

"""
二叉搜索树 - AVL tree
空节点 height = -1
h(left) - h(right) <= |1|
"""
class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        # self.height = 0
        # self.bf = -1

    def distroy(self):
        self.left = None
        self.right = None
        self.parent = None

class AVL(object):
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return -1
        else:
            return node.height

    def update_height(self, node):
        node.height = max(self.height(node.left), self.height(node.right)) + 1

    def insert(self, data):
        """
        非递归插入节点
        :param data:
        :return:
        """
        new = Node(data)
        if self.root is None:
            self.root = new
        else:
            node = self.root
            while True:
                if node.data > data:
                    if  node.left is None:
                        node.left = new
                        new.parent = node
                        break
                    node = node.left
                else:
                    if node.right is None:
                        node.right = new
                        new.parent = node
                        break
                    node = node.right

        return new

    def insert_then_rebalance(self, data):
        """
        插入节点后并平衡
        :param data:
        :return:
        """
        node = self.insert(data)
        self.rebalance(node)

    def find(self, data):
        """
        查找某个节点
        :param data:
        :return:
        """
        node = self.root
        while node:
            if node.data == data:
                return node
            elif node.data > data:
                node = node.left
            elif node.data < data:
                node = node.right
            else:
                return None
        return None

    def delete_min(self):
        """
        非递归删除最小节点
        :return:
        """
        if not self.root:
            return None, None
        else:
            node = self.root
            while node.left: #最左边节点是最小的节点
                node = node.left
            if node.parent: #存在父节点
                node.parent.left = node.right #把要删除的节点的右节点给要删除节点父节点的左节点
            else: #不存在父节点肯定是最小树
                self.root = node.right #直接把要删除节点的右节点作为根节点
            if node.right: #要删除节点的右节点存在
                node.right.parent = node.parent #把要删除节点的父节点作为要删除节点右节点的父节点
            parent = node.parent
            node.destroy()
            return node, parent


    def left_rotate(self, node):
        """
                 node(h=2)
                /         \
               y(h=0)     x (h=1)
              /  \      /      \
                        z(h=-1) m (h=0)
                       /\      /\
                                i(h=0)
        :param node:
        :return:
        """
        x = node.right
        x.parent = node.parent
        if x.parent is None: #如果没有父节点 则为根节点
            self.root = x
        else:
            if x.parent.left is node: #如果之前node节点是其父节点的左节点
                x.parent.left = x #则转换后的x也要是其父节点的左节点
            elif x.parent.right is node: #如果之前node节点是其父节点的右节点
                x.parent.right = x #则转换后的x也要是其父节点的右节点
        node.right = x.left #x节点的左几点成为node节点的右节点
        if node.right: #如果node节点新右节点存在
            node.right.parent = node #则node新右节点的父节点为node
        x.left = node #node变为x的左节点
        node.parent = x #旋转后的node的父节点应为x
        self.update_height(node)
        self.update_height(x)

    def right_rotate(self, node):
        """
             node(h=2)
            /      \
           y(h=1)   x(h=0)
          /     \      /\
        z(h=1)  m(h=0)
         / \
        i(h=0)
        :param node:
        :return:
        """

        y = node.left
        y.parent = node.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is node:
                y.parent.left = y
            elif y.parent.right is node:
                y.parent.right = y
        node.left = y.right
        if node.left:
            node.left.parent = node
        y.right = node
        node.parent = y
        self.update_height(node)
        self.update_height(y)


    def rebalance(self, node):
        while node is not None:
            self.update_height(node) #更新当前节点的高度
            if self.height(node.left)  >= 2 + self.height(node.right):#如果当前节点的左边高度-右边高度>=2
                if self.height(node.left.left) >= self.height(node.left.right):#如果当前节点左边的左边高度-当前节点右边的右边高度>0 为LL 进行右旋转
                    self.right_rotate(node)
                else:#否则为 LR 先进行左旋转再进行右旋转
                    self.left_rotate(node.left)
                    self.right_rotate(node)

            elif self.height(node.right)  >= 2 + self.height(node.left): #如果当前节点右边高度-左边高度>=2
                if self.height(node.right.right)  >= self.height(node.right.left): #如果当前节点右边的右边高度-当前节点左边的左边高度>0 为RR 进行左旋转
                    self.left_rotate(node)
                else: #否则为 RL 先进行右旋转再左旋转
                    self.right_rotate(node.right)
                    self.left_rotate(node)
            node = node.parent #沿着插入节点向上路径重复操作


    def __str__(self):
        if self.root is None: return '<empty tree>'
        def recurse(node):
            if node is None: return [], 0, 0
            label = str(node.data)
            left_lines, left_pos, left_width = recurse(node.left)
            right_lines, right_pos, right_width = recurse(node.right)

            middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
            pos = left_pos + middle // 2
            width = left_pos + middle + right_width - right_pos
            while len(left_lines) < len(right_lines):
                left_lines.append(' ' * left_width)
            while len(right_lines) < len(left_lines):
                right_lines.append(' ' * right_width)
            if (middle - len(label)) % 2 == 1 and node.parent is not None and \
               node is node.parent.left and len(label) < middle:
                label += '.'
            label = label.center(middle, '.')
            if label[0] == '.': label = ' ' + label[1:]
            if label[-1] == '.': label = label[:-1] + ' '
            lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
                     ' ' * left_pos + '/' + ' ' * (middle-2) +
                     '\\' + ' ' * (right_width - right_pos)] + \
              [left_line + ' ' * (width - left_width - right_width) +
               right_line
               for left_line, right_line in zip(left_lines, right_lines)]
            return lines, pos, width
        return '\n'.join(recurse(self.root) [0])

import random
avl = AVL()
for item in (random.randrange(100) for i in xrange(int(50))):
        avl.insert2(item)

print (avl)
