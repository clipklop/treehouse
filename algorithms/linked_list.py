# *
# *** Linked list implementations
# *

class Node:
    """
    An object for storing a single node of a linked list.
    Models two attribute - data and the link to the next list
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data


node = Node('yo')
print(node.next_node)
