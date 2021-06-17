class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        node = Node(data)

        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

class HashMap:
    def __init__(self, size=1024):
        self.size=size
        self.map = self.size * [None]

    
    def _hash(self, key):
        hashed_total = 0
        for char in key:
            hashed_total += ord(char)
        return hashed_total*19 % self.size


    def add(self,key,value):
        key_hash = self._hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
                else:
                    self.map[key_hash].append(list([key_value]))
                    return True

    def get(self,key):
        key_hash = self.hash(key) 
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]: 
                if pair[0] == key:
                    return pair[1]


    def set(self,key,value):
        hashed_key = self.hash(key)
        if self.map[hashed_key] == None:
            self.map[hashed_key] = LinkedList()
        self.map[hashed_key].add((key, value))

    