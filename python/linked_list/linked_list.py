class Node:

    def __init__(self, value=None):
        self.value = value
        self.next = None
  # use a magic method so when you print node you see it's value
    def __str__(self):
        return self.value

# Define linked list
class LinkedList():

    # Constructor
    def __init__(self):
        self.head = None
    # define my insert method
    def insert (self, data):
        new_node = Node(data)
    # Once we have a head 
        if self.head :
            # set our current pointer to the head
            current = self.head 
            # while there is a following node that's not None
            while (current.next):
                # move to the next node
                current = current.next
      
                # Assign new_node to current.next
            current.next = new_node
        else:
            #Assign new_node to self.head 
            self.head = new_node

    def include(self, value):
        """method to check if the given value is in the linked list"""
        current = self.head
        while current:
            if current.value == value:
                return True
            else:
                current = current.next
        return False
    # __str__ , __repr__
    def __str__(self):
        """ returns a string representing all the values in the Linked List, formatted as:
        "{ a } -> { b } -> { c } -> NULL"
        """
        # step 0 - create a new empty string
        output = ""

        # step 1 iterate over each node
        current = self.head
        while current:
        # step 2 - append each value to the string
            output += f"{{ {current.value} }} -> "
            # step 2b:  move to the next item
            current = current.next
        output += " Null"

        # step 3 - return the final string
        return output