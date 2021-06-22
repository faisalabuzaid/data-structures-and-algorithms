
import re

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
            print('test add')
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

def repeat(input): 
    
    words = re.findall('[\w]+', input.lower())
    table = HashMap()

    for word in words:

        if table.contains(word):
            table.add(word, table.get(word)+1)
        else:
            table.add(word, 1)
    return table
      
if __name__ == "__main__": 
    input ="Once upon a time, there was a brave princess who..."
    # actual = repeat(input).get('a')
    # print(actual)


    input2 ="It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    actual = repeat(input2).get('was')
    print(actual) 

    input3 ="It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    # repeat(input3)