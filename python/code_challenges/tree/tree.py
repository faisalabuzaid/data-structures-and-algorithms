class Queue:
    def __init__(self):
        self.front = None

    def enqueue(self, data):
        node = Node(data)

        if not self.front:
            self.front = node
        else:
            current = self.front
            while current.next:
                current = current.next
            current.next = node
            node.next = None

    def dequeue(self):
        if not self.isEmpty():
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp.data
        return "empty"

    def isEmpty(self):
        if self.front:
            return False
        return True

class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None
        self.next = None

class BinaryTree:
    def __init__(self, root = None):
        self.root = Node(root)

    def preOrder(self):
        tree = []

        if self.root:

            def walk(node):

                tree.append(node.data)

                if node.left:
                    walk(node.left)

                if node.right:
                    walk(node.right)

            walk(self.root)
            return tree

        else:
            return "tree is empty"

    def inOrder(self):
        tree = []

        if self.root:

            def walk(node):

                if node.left:
                    walk(node.left)

                tree.append(node.data)

                if node.right:
                    walk(node.right)

            walk(self.root)
            return tree

        else:
            return "tree is empty"

    def postOrder(self):
        tree = []

        if self.root:

            def walk(node):

                if node.left:
                    walk(node.left)

                if node.right:
                    walk(node.right)

                tree.append(node.data)

            walk(self.root)
            return tree

        else:
            return "tree is empty"

    def find_maximum_value(self):
       
        maximum_value = self.root.data

        def walk(root):

            nonlocal maximum_value

            if root.data > maximum_value:
                maximum_value = root.data

            if root.left:
                walk(root.left)

            if root.right:
                walk(root.right)

            return maximum_value

        return walk(self.root)

    def breadth_first(self):
        q = Queue()

        q.enqueue(self.root)

        result = []

        temp = None

        while not q.isEmpty():

            temp = q.dequeue()

            result.append(temp.data)

            if temp.left:
                q.enqueue(temp.left)

            if temp.right:
                q.enqueue(temp.right)

        return result

class BinarySearchTree(BinaryTree):

    def add(self, data):

        if not self.root:
            self.root = Node(data)

        else:
            def walk(root):
                if data < root.data:
                    if not root.left:
                        root.left = Node(data)
                        return
                    else:
                        walk(root.left)
                else:
                    if not root.right:
                        root.right = Node(data)
                        return
                    else:
                        walk(root.right)

            return walk(self.root)

    def contains(self, data):
        
        while self.root:

            if self.root.data == data:
                return True

            elif self.root.data > data:
                if self.root.left:
                    self.root = self.root.left
                else: 
                    return False

            else:
                if self.root.right:
                    self.root = self.root.right
                else: 
                    return False

        return False

if __name__ == "__main__":
    
    tree = BinaryTree(10)
    tree.root.left = Node(90)
    tree.root.left.left = Node(27)
    tree.root.left.right = Node(8)
    tree.root.right = Node(16)
    tree.root.right.left= Node(11)
    tree.root.right.right = Node(97)
    print(tree.find_maximum_value())
    print(tree.inOrder())
    print(tree.breadth_first())

