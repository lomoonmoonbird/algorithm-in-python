# --*-- coding: utf-8 --*--

"""
资料:http://algs4.cs.princeton.edu/32bst/
"""

class Node(object):
    '''
    节点类 构造节点
    '''
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0
        self.balance = 0
        self.size = 1

    def destroy(self):
        self.left = None
        self.right = None
        self.parent = None

    def node_size(self, node):
        if not node:
            return 0
        else:
            return node.size

    def update_size(self, node):
        node.size = self.node_size(node.left) + self.node_size(node.right)

    def rank(self, data):
        """
        计算当前几点在树中的第几个节点
        :param data:
        :return:
        """
        left_size = 0 if self.left is None else self.left.size #先计算左边节点的size
        if data == self.data:
            pass
        #todo


class BST(object):
    '''
    二叉搜索树
    '''
    def __init__(self):
        self.root = None

    def insert_non_recursive(self, data):
        """
        非递归循环插入节点
        :param data:
        :return:
        """
        new = Node(data)

        if not self.root:
            self.root = new

        else:

            node = self.root
            while True:
                if data < node.data: #插入节点数据小于当前根节点 应插入当前节点左边
                    if not node.left: #如果当前节点无左节点 则直接插入左节点
                        node.left = new
                        new.parent = node
                        break
                    node = node.left
                elif data > node.data: #插入节点大于当前节点 应插入当前节点右边
                    if not node.right: #如果当前节点无右节点 则直接插入右节点
                        node.right = new
                        new.parent = node
                        break
                    node = node.right
                else: #不存在节点相等
                    break

            #更新树的size
            while node is not None:
                self._update_size(node)
                node = node.parent
        return new

    def insert_recursive(self, node, data):
        """
        递归插入某个节点
        :param node:
        :param data:
        :return:
        """
        new = Node(data)
        if not self.root:
            self.root = node
        else:
            if data < node.data:
                if not node.left:
                    node.left = new
                else:
                    self.insert_recursive(node.left, data)
            elif data > node.data:
                if not node.right:
                    node.right = new
                else:
                    self.insert_recursive(node.right, data)
            else:
                return None

    def insert_with_size_non_recursive(self, data):
        """
        非递归更新树的规模
        :param data:
        :return:
        """
        node = self.insert_non_recursive(data)
        while node:
            node.update_size(node)
            node = node.parent

    def _update_size(self, node):
        while node:
            node.update_size(node)
            node = node.parent



    def leftmost_of_right_tree(self, node):
        """
        返回右子树最左边节点
        :param node: right node
        :return:
        """
        current = node
        while current.left is not None:
            current = current.left
        return current

    def rightmost_of_left_tree(self, node):
        """
        返回左子树最右边节点
        :param node:
        :return:
        """
        current = node
        while current.right is not None:
            current = current.right
        return current

    def delete(self, node, data):
        """
        递归删除某个节点
        :param node:
        :param data:
        :return:
        """
        if self.root is None:
            return self.root
        if data < node.data: #如果找不到要删除的节点,如果删除的数据小于当前节点,则继续向当前节点的左节点继续删除
            node.left = self.delete(node.left, data)
        elif data > node.data: #如果找不到要删除的节点,如果删除的数据大于当前节点,则继续向当前节点的右节点继续删除
            node.right = self.delete(node.right, data)
        else: #如果找到要删除的节点,则需要看要删除的节点1:是叶子节点,2:只要一个孩子节点(分左孩子和右孩子),3:有两个孩子节点
            if node.left is None: #没有左孩子,有右孩子或者没有
                tmp = node.right
                node = None
                return tmp
            elif node.right is None: #没有右孩子,有左孩子或者没有
                tmp = node.left
                node = None
                return tmp
            else: #左孩子右孩子都有
                min_node = self.leftmost_of_right_tree(node.right) #拿到要删除节点的右子树中序最小节点
                node.data = min_node.data #将最小节点替换要删除的节点
                node.right = self.delete(node.right, min_node.data) #再次递归删除此最小节点
        return node

    def delete_min_non_recursive(self):
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

    def delete_min_with_size_non_recursive(self):
        deleted, parent = self.delete_min_non_recursive()
        node = parent
        while node:
            node.update_size(node)
            node = node.parent
        return deleted, parent

    def find_non_recursive(self, data):
        """
        非递归查找某个节点
        :param data:
        :return:
        """
        node = self.root
        while node:
            if node.data == data:
                return node
            elif node.data > data: #左节点
                node = node.left
            else: #右节点
                node = node.right
        return node

    def find_recursive(self, node, data):
        """
        递归查找某个节点
        :param node:
        :param data:
        :return:
        """
        if not node:
            return None
        if node.data == data:
            return node
        elif node.data > data:
            # print node.left.__dict__
            return self.find_recursive(node.left, data)
        else:
            # print node.right.__dict__
            return self.find_recursive(node.right, data)




    def pre_order(self, node):
        """
        前序遍历
        :param node:
        :return:
        """
        if not node:
            return None
        print (node.data, node.size)
        self.pre_order(node.left)
        self.pre_order(node.right)

    def in_order(self, node):
        """
        中序遍历
        :param node:
        :return:
        """
        if not node:
            return None
        self.in_order(node.left)
        print (node.data)
        self.in_order(node.right)


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


bst = BST()
[bst.insert_with_size_non_recursive(data) for data in [6,7,5,2,4,1]]
print (bst)
print (bst.pre_order(bst.root))
bst.delete(bst.root, 6)
print (bst)
#
# bst.delete_min_with_size_non_recursive()
# print bst
# print bst.pre_order(bst.root)
