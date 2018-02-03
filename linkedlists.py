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

    # This function prints contents of linked list
    # starting from head
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data,)
            temp = temp.next

    # Function to insert a new node at the beginning
    def push(self, new_data):
        # 1 & 2: Allocate the Node &
        #        Put in the data
        new_node = Node(new_data)
        # 3. Make next of new Node as head
        new_node.next = self.head
        # 4. Move the head to point to new Node
        self.head = new_node

    # Inserts a new node after the given prev_node.
    def insertAfter(self, prev_node, new_data):
    # 1. check if the given prev_node exists
    if prev_node is None:
        print "The given previous node must inLinkedList."
        return
    #  2. Create new node &
    #  3. Put in the data
    new_node = Node(new_data)
    # 4. Make next of new Node as next of prev_node
    new_node.next = prev_node.next
    # 5. make next of prev_node as new_node
    prev_node.next = new_node


# main run
if __name__ == '__main__':

        # Initialize list head
        linkList = LinkedList()

        # Define head of List
        linkList.head = Node(1)
        # Make two more nodes
        scdNode = Node(2)
        thdNode = Node(3)

        # Link Nodes
        linkList.head.next = scdNode
        scdNode.next = thdNode

        linkList.printList()
