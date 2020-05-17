"""
Given a Binary Tree find the length of the longest path which comprises of nodes with consecutive values in increasing order.
Every node is considered as a path of length 1.
"""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add_node(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = TreeNode(value)
                else:
                    self.left.add_node(value)
            else:
                if self.right is None:
                    self.right = TreeNode(value)
                else:
                    self.right.add_node(value)
        else:
            self.value = value


class FindSequence:
    
    def longest_sequence_driver(self, treeNode):
        maxlen = [0]
        interim = 0
        interim, maxlen = self.longest_sequence(treeNode, None, interim, maxlen)
        return maxlen

    def longest_sequence(self, currentNode, parentNode, interim, maxlen):
        """
        Find the length of longest consecutive path
        """
        if currentNode is None:
            return 0
        print("currently scanning {}, interim value is {}".format(currentNode.value, interim))

        interim += self.longest_sequence(currentNode.left, currentNode, interim, maxlen)
        interim += self.longest_sequence(currentNode.right, currentNode, interim, maxlen)
        print("interim = {}".format(interim))
        if parentNode is None:
            return

        if parentNode.value + 1 == currentNode.value:
            print("{} is consecutive to {} returning 1".format(currentNode.value, parentNode.value))
            return 1
        else:
            if interim + 1 > maxlen[0]:
                maxlen[0] = interim + 1
                print("maxlen = {}".format(maxlen))
            interim = 0
        return


if __name__ == "__main__":
    root = TreeNode(6)
    root.add_node(9)
    root.add_node(10)
    root.add_node(11)
    find_seq = FindSequence()

    print(find_seq.longest_sequence_driver(root))
