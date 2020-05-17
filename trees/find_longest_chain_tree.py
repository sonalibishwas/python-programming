"""
chain = all left most nodes + all rights most nodes + 1
"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_node(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = TreeNode(data)
                else:
                    self.left.add_node(data)
            else:
                if self.right is None:
                    self.right = TreeNode(data)
                else:
                    self.right.add_node(data)
        else:
            self.data = data

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()


def find_chain(root):
    maxlen = float("-inf")
    x, maxlen = find_chain_helper(root, "root", maxlen)
    print("maxlen={}".format(maxlen))


def find_chain_helper(node, called_with, maxlen):
    if node is None:
        return 0,maxlen
    left_count, maxlen = find_chain_helper(node.left,"left", maxlen)
    right_count, maxlen = find_chain_helper(node.right,"right", maxlen)
    chain_length = left_count + right_count + 1
    print("chain length = {}".format(chain_length))
    if chain_length > maxlen:
        maxlen = chain_length
    if called_with == "left":
        print("returning leftcount = {}, maxlen = {}".format(left_count + 1, maxlen))
        return left_count + 1, maxlen
    else:
        print("returning rightcount = {}, maxlen = {}".format(right_count + 1, maxlen))
        return right_count + 1, maxlen


if __name__ == "__main__":
    root = TreeNode(9)
    root.add_node(2)
    root.add_node(10)
    root.add_node(1)
    root.add_node(3)
    root.add_node(0)
    root.add_node(11)
    root.print_tree()
    find_chain(root)
