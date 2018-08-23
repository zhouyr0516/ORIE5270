import unittest
from Tree.Tree import *

class TestTrees(unittest.TestCase):

    def test_1(self):
        t = Tree(Node(1, None, None))
        assert t.print_tree() == [['1']]

    def test_2(self):
        a = Node(1, None, None)
        a.left = Node(2, Node(4, None, None), Node(5, None, None))
        a.right = Node(3, Node(6, None, None), Node(7, None, None))
        t = Tree(a)
        assert t.print_tree() == [['|', '|', '|', '1', '|', '|', '|'],
                                  ['|', '2', '|', '|', '|', '3', '|'],
                                  ['4', '|', '5', '|', '6', '|', '7']]

    def test_3(self):
        a = Node(1, None, None)
        a.left = Node(2, None, None)
        a.left.left = Node(3, None, None)
        a.left.left.left = Node(4, None, None)
        t = Tree(a)
        assert t.print_tree() == [['|', '|', '|', '|', '|', '|', '|', '1', '|', '|', '|', '|', '|', '|', '|'],
                                  ['|', '|', '|', '2', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|'],
                                  ['|', '3', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|'],
                                  ['4', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|']]

    def test_4(self):
        a = Node(1, None, None)
        a.left = Node(2, None, None)
        a.right = Node(3, None, None)
        a.left.right = Node(4, None, None)
        a.right.left = Node(5, None, None)
        a.right.left.right = Node(6, None, None)
        t = Tree(a)
        assert t.print_tree() == [['|', '|', '|', '|', '|', '|', '|', '1', '|', '|', '|', '|', '|', '|', '|'],
                                  ['|', '|', '|', '2', '|', '|', '|', '|', '|', '|', '|', '3', '|', '|', '|'],
                                  ['|', '|', '|', '|', '|', '4', '|', '|', '|', '5', '|', '|', '|', '|', '|'],
                                  ['|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '6', '|', '|', '|', '|']]

if __name__ == '__main__':
    unittest.main()
