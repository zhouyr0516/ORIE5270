import unittest
from tree.tree import Tree, Node


class TestTrees(unittest.TestCase):

    def test_1(self):
        t = Tree(Node(1, None, None))
        assert t.print_tree() == [['1']]

    def test_2(self):
        node = Node(1, None, None)
        node.left = Node(2, Node(4, None, None), Node(5, None, None))
        node.right = Node(3, Node(6, None, None), Node(7, None, None))
        t = Tree(node)
        assert t.print_tree() == [['|', '|', '|', '1', '|', '|', '|'],
                                  ['|', '2', '|', '|', '|', '3', '|'],
                                  ['4', '|', '5', '|', '6', '|', '7']]

    def test_3(self):
        node = Node(1, None, None)
        node.left = Node(2, None, None)
        node.left.left = Node(3, None, None)
        node.left.left.left = Node(4, None, None)
        t = Tree(node)
        assert t.print_tree() == [['|', '|', '|', '|', '|', '|', '|',
                                   '1', '|', '|', '|', '|', '|', '|', '|'],
                                  ['|', '|', '|', '2', '|', '|', '|',
                                   '|', '|', '|', '|', '|', '|', '|', '|'],
                                  ['|', '3', '|', '|', '|', '|', '|',
                                   '|', '|', '|', '|', '|', '|', '|', '|'],
                                  ['4', '|', '|', '|', '|', '|', '|',
                                   '|', '|', '|', '|', '|', '|', '|', '|']]

    def test_4(self):
        node = Node(1, None, None)
        node.left = Node(2, None, None)
        node.right = Node(3, None, None)
        node.left.right = Node(4, None, None)
        node.right.left = Node(5, None, None)
        node.right.left.right = Node(6, None, None)
        t = Tree(node)
        assert t.print_tree() == [['|', '|', '|', '|', '|', '|', '|',
                                   '1', '|', '|', '|', '|', '|', '|', '|'],
                                  ['|', '|', '|', '2', '|', '|', '|',
                                   '|', '|', '|', '|', '3', '|', '|', '|'],
                                  ['|', '|', '|', '|', '|', '4', '|',
                                   '|', '|', '5', '|', '|', '|', '|', '|'],
                                  ['|', '|', '|', '|', '|', '|', '|',
                                   '|', '|', '|', '6', '|', '|', '|', '|']]


if __name__ == '__main__':
    unittest.main()
