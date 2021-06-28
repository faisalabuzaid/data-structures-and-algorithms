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

    def __str__(self) -> str:
        result = ""
        current = self.head
        while current:
            result += str(current.value)
        return f"{result} > None"

class HashMap:
    def __init__(self, size=1024):
        self.size=size
        self.bucket = self.size * [None]
    
    def _hash(self, key):
        sum = 0
        for char in key:
            sum += ord(char)
        return sum*19 % self.size


    def add(self,key,value):

        index = self._hash(key)

        if not self.bucket[index]:
            self.bucket[index] = LinkedList()
          
        current = self.bucket[index].head
        while current:
            if current.value[0] == key:
                current.value[1] = value
                return
            current = current.next
        self.bucket[index].add([key, value])


    def get(self,key):
        index = self._hash(key) 
        if self.bucket[index]:
            current = self.bucket[index].head
            while current:
                if current.value[0] == key:
                    return current.value[1]
                current = current.next
        # raise KeyError('Key is not found')
        return 'Null'

    def contains(self,key):
        index = self._hash(key)
        if self.bucket[index]:
            current = self.bucket[index].head
            while current:
                if current.value[0] == key:
                    return True
        return False
    # def __str__(self):
    #     result =""
    #     for i in range(self.size):
    #         result += f"{self.bucket[i]}, "
    #     return result
# test = HashMap()
# test.add('ab', 'faisal')
# test.add('ba', 'ahmad')

# print(test._hash('ab'))
# print(test._hash('ba'))

# print(test.get('ab'))
# print(test.get('ba'))

# table1 = HashMap()
# table1.add("faisal", 1)
# table1.add('lara','ahmad')
# table1.add('sara','ahmad')
# table2 = HashMap()
# table1.add('faisal','abuzaid')
# table1.add('lara','abuzaid')
# table1.add('sara','abuzaid')
# print(table1)