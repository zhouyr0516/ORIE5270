class Tree(object):

    def __init__(self, root):
        self.root = root

    def get_value_root(self):
        if not self.root:
            return self.root.value
        else:
            return None

    def depth(self):

        if not self.root:
            return 0
        elif not self.root.left and not self.root.right:
            return 1
        else:
            left_subtree = Tree(self.root.left)
            right_subtree = Tree(self.root.right)
            return 1 + max(left_subtree.depth(), right_subtree.depth())

    def print_tree(self):
        d = self.depth()
        q = [self.root]
        depth_count = 0
        res_mat = [[0]*(2**d - 1) for i in range(d)]

        for idx in range(d):
            row_idx = 0
            new_q = []
            for i in range(2 ** (d - depth_count - 1) - 1):
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

            for i in range(2 ** (d - depth_count - 1) - 1):
                res_mat[idx][row_idx] = '|'
                row_idx = row_idx + 1

            print('')
            depth_count = depth_count + 1
            q = new_q

        for row_idx in range(d):
            for i in range(2**d-1):
                print(res_mat[row_idx][i], end='')
            print('')

        return res_mat

class Node(object):

    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right



