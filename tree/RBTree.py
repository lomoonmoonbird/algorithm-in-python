#--*-- coding:utf-8 --*--

from enum import Enum

class Color(Enum):
    Red = 0
    Black = 1

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.color = Color.Red.value

    def distroy(self):
        self.left = None
        self.right = None
        self.data = None


class RDTree(object):

    def __init__(self):
        self.root = None

    def insert(self, data):
        new = Node(data)

        while True:
            if self.root is None:
                self.root = new
            else:
                node = self.root
                if data < node.data:
                    if node.left is None:
                        node.left = new
                        break
                    else:
                        node = node.left
                elif data > node.data:
                    if node.right is None:
                        node.right = new
                        break
                    else:
                        node = node.right
                else:
                    break

        return new

    def delete(self, node, data):
        if self.root is None:
            return self.root
        elif node.data > data:
            self.delete(node.left, data)
        elif node.data < data:
            self.delete(node.right, data)
        else:
            if node.left is None:
                tmp = node.right
                node = None
                return tmp
            if node.right is None:
                tmp = node.left
                node = None
                return tmp
            min_leaf_node = self.min_node(node)


    def min_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current