class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


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
    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __str__(self) -> str:
        result = ""
        current = self.head
        while current:
            result += f"{current.value} "
            current = current.next
        return result


class HashMap:
    def __init__(self, size=1024):
        self.size = size
        self.bucket = self.size * [None]

    def _hash(self, key):
        sum = 0
        for char in key:
            sum += ord(char)
        return sum * 19 % self.size

    def add(self, key, value):

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
    

    def get(self, key):
        index = self._hash(key)
        if self.bucket[index]:
            current = self.bucket[index].head
            while current:
                if current.value[0] == key:
                    return current.value[1]
                current = current.next
        # raise KeyError('Key is not found')
        return "Null"

    def contains(self, key):
        index = self._hash(key)
        if self.bucket[index]:
            current = self.bucket[index].head
            while current:
                if current.value[0] == key:
                    return True
                current = current.next
        return False

    def __iter__(self):
        for items in self.bucket:
            if items:
                for value in items:
                    yield value

    def __str__(self) -> str:
        result = ''
        for item in self:
            result += f"{item} "
        return result


def most_common(paragraph):


    words_list = paragraph.split()
    mytable = HashMap()
    for word in words_list:

        if mytable.contains(word):
            mytable.add(word, mytable.get(word)+1)
        else:
            mytable.add(word,1)

    initial = 0
    for item in mytable:
        if item[1] > initial:
            initial = item[1]
            word = item[0]
    return word 


if __name__ == '__main__':
  test = 'in a galaxy far far away'
  print(most_common(test))

