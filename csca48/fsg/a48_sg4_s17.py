# readings available here:
# http://openbookproject.net/thinkcs/python/english3e/linked_lists.html

class DLLNode():

    def __init__(self, data, next=None, prev=None):
        # note how these variables are not private. This is one way of
        # implementing this class
        self.data = data
        self.next = next
        self.prev = prev

    # define how nodes behave when printed
    def __str__(self):
        return str(self.data)

    # similar to printing the node, but in a way that can be read by the
    # computer. You can read more about this here:
    # https://docs.python.org/3/library/functions.html#repr
    def __repr__(self):
        return str(self.data)

def remove_index(head, index):
    '''(DLLNode, int) -> NoneType
    Removes the node in the linked list at the given index
    '''
    # first we set the head
    curr = head
    # we go through the list, stopping one before the node we want to remove
    for i in range(index - 1):
        # we are constantly going to the next node
        curr = curr.next
    # identify the node that comes after the node we want to remove
    node_remove_next = curr.next.next
    # set the next pointer of the node we want to remove to None
    curr.next.next = None
    # set the next pointer of the current node to the node after the one
    # we want to remove
    curr.next = node_remove_next
    return head

if __name__ == "__main__":
    # this is a fast way of instantiating a bunch of nodes
    # and setting their pointers
    node_count = 15
    nodes = []
    # create all the nodes
    for i in range(node_count):
        nodes.append(DLLNode(i))

    # link all the nodes
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i+1]
        nodes[i+1].prev = nodes[i]

    print(nodes)
    head = remove_index(nodes[0], 12)
    linked_list = []
    curr = head
    # add all the nodes to our new list
    # this list represents our linked list after the removal
    # we are only using this to display the values
    while curr is not None:
        linked_list.append(curr)
        curr = curr.next
    print(linked_list)

