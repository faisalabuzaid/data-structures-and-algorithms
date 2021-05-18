
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



    def insert_after(self, value, new_data):
        if self.include(value):
            current = self.head
            while current:
                if current.value == value:
                    node = Node(new_data)
                    node.next = current.next
                    current.next = node
                    return self.__str__()
                current = current.next
        else:
            return 'Value is not in the list'
    
        
    def insert_before(self, search_value, new_value):
        if self.head == None:
          return "The value is not exist"

        new_node = Node(new_value)
        current = self.head
        if search_value == current.value:
          self.head = new_node
          self.head.next = current
          return "The search value is not exist"
        while current.next:
          if current.next.value == search_value:
            new_node.next = current.next
            current.next = new_node
            break
          current = current.next

    def kthFromEnd(self, k):
        current = self.head
        count = 0
        
        while current.next:
            current = current.next
            count += 1

        if k > count:
            return("Sorry, the value is larger than the linked list")

        if k > count:
            raise Exception("Sorry, the value is larger than the linked list")
      

        current = self.head
        for i in range(count - k):
            current = current.next
        print(current.value)
        return current.value

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

test = LinkedList()
test.insert(1)
print(test)
test.append(2)
print(test)
test.insert_after(1,10)
print(test)
test.insert_before(2, 4)
print(test)

def linked_list():
    linked_list = LinkedList()
    new_nodes = ['I', 'am', 'here', 'and', ['a', 'l', 'i', 7, 3]]
    for node in new_nodes:
        linked_list.insert(node)
    return linked_list

print(linked_list())
test=linked_list()
test.insert_before("and",3)
print(test)