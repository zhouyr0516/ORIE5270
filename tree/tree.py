class Tree(object):
    """
    Tree object composed by Nodes class
    """
    def __init__(self, root):
        self.root = root

    def get_value_root(self):
        """
        get the value of the root node
        :return:
        """
        if not self.root:
            return self.root.value
        else:
            return None

    def depth(self):
        """
        get the depth of the tree
        :return: int depth of the tree
        """
        if not self.root:
            return 0
        elif not self.root.left and not self.root.right:
            return 1
        else:
            left_subtree = Tree(self.root.left)
            right_subtree = Tree(self.root.right)
            return 1 + max(left_subtree.depth(), right_subtree.depth())

    def print_tree(self):
        """
        print the tree in matrix form
        :return: the visualization of tree
        """
        d = self.depth()
        q = [self.root]
        depth_count = 0
        res_mat = [[0]*(2**d - 1) for i in range(d)]

        for idx in range(d):
            row_idx = 0
            new_q = []
            num_blank = 2**(d-depth_count-1) - 1
            for i in range(num_blank):
                res_mat[idx][row_idx] = '|'
                row_idx = row_idx + 1

            for x in q:
                if not x:
                    res_mat[idx][row_idx] = '|'
                    new_q.append(None)
                    new_q.append(None)
                else:
                    res_mat[idx][row_idx] = str(x.value)
                    new_q.append(x.left)
                    new_q.append(x.right)
                row_idx = row_idx + 1
                if len(q) > 1:
                    for i in range(2 ** (d - depth_count) - 1):
                        res_mat[idx][row_idx] = '|'
                        row_idx = row_idx + 1
                q = q[1:]

            for i in range(num_blank):
                res_mat[idx][row_idx] = '|'
                row_idx = row_idx + 1

            print('')
            depth_count = depth_count + 1
            q = new_q

        for row_idx in range(d):
            for j in range(2**d-1):
                print(res_mat[row_idx][j]),
            print('')

        return res_mat


class Node(object):
    """
    Node class that has left and right leaves
    """
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
