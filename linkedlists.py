# Node class
class Node:

    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize
                          # next as null

# Linked List class
class LinkedList:

    # Function to initialize the Linked
    # List object
    def __init__(self):
        self.head = None

# main run
if __name__ == '__main__':

        # Initialize list head
        linkList = Node(1)

        # Define head of List
        linkList.head = Node(1)
        # Make two more nodes

        scdNode = Node(2)
        thdNode = Node(3)

        '''
        from https://www.geeksforgeeks.org/linked-list-set-1-introduction

        Three nodes have been created.
        We have references to these three blocks as first,
        second and third

        llist.head        second              third
             |                |                  |
             |                |                  |
        +----+------+     +----+------+     +----+------+
        | 1  | None |     | 2  | None |     |  3 | None |
        +----+------+     +----+------+     +----+------+
        '''

        # Link Nodes
        linkList.head.next = scdNode
        '''
        Now next of first Node refers to second.  So they
        both are linked.

        llist.head        second              third
             |                |                  |
             |                |                  |
        +----+------+     +----+------+     +----+------+
        | 1  |  o-------->| 2  | null |     |  3 | null |
        +----+------+     +----+------+     +----+------+
        '''
        scdNode.next = thdNode

        '''
        Now next of second Node refers to third.  So all three
        nodes are linked.

        llist.head        second              third
         |                |                  |
         |                |                  |
        +----+------+     +----+------+     +----+------+
        | 1  |  o-------->| 2  |  o-------->|  3 | null |
        +----+------+     +----+------+     +----+------+
        '''
