class Node:

    def __init__(self, value=None, next=None):
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
        new_node.next = self.head
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
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            current = last.next
        last.next = new_node



    def insertAfter(self, prev_node, new_data):
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def insertBefore(self, next_node, value):
        if (self.head == next_node):
  
            # Create a node
            n = Node(value)
    
            # Point to next to current head
            n.next = self.head
    
            # Update the head pointer
            head = n
      
    # Otherwise traverse the list to
    # find previous node of given node
        else:
    
            p = None
            n = self.head
    
            # This loop will return p with
            # previous pointer of given node
            while(n != next_node):
                p = n
                n = n.next
    
            # Create a node
            m = Node(value)
    
            # Update the m.next
            m.next = p.next
    
            # Update previous node's next
            p.next = m


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

