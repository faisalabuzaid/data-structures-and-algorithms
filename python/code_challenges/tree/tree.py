from typing import Counter

class Node():
    def __init__(self, value=None):
        self.value = value
        self.next = None

class TNode:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None



class Queue():
    def __init__(self, front=None, rear=None):
        self.front = front
        self.rear = rear

    def enqueue(self, value):
        node  = Node(value)
        if not self.rear:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.front:
            previous = self.front
            self.front = self.front.next
            return previous.value
        raise Exception("You can't dequeue from empty Queue")

    def peek(self):
        if self.front:
            return self.front.value
        raise Exception("Empty Queue")


    def isEmpty(self):
        if not self.front:
            return True
        return False

    def __str__(self):
        current = self.front
        items = []
        while current:
            items.append(str(current.value))
            current = current.next
        return "\n".join(items)

class Binary_Tree:
    def __init__(self,root):
        self.root=TNode(root)


    def pre_order(self):
        result=[]
        def walk(current):
            """
            ROOT -> LEFT -> RIGHT.
            """
            if current:
                result.append(str(current.value))
            if current.left:    
                walk(current.left)
            if current.right:
                walk(current.right)
        walk(self.root)
        return result
        


    def in_order(self):
        """
         LEFT-> ROOT -> RIGHT.
        """
        result=[]
        def walk(current):
            if current:
                if current.left:
                    walk(current.left)
                result.append(str(current.value))
                if current.right:
                    walk(current.right)
        walk(self.root)
        return result

    def post_order(self):
        """
          LEFT -->> RIGHT -->> ROOT.
        """
        result=[]
        def walk(current):
            if current:
                if current.left:
                    walk(current.left)
                if current.right:
                    walk(current.right)
                result.append(str(current.value))
        walk(self.root)
        return result

    def find_max(self):
        self.value=0
        def walk(current):
            if current:
                if current.value > self.value:
                    self.value = current.value
                if current.right:
                        walk(current.right)
                if current.left:
                        walk(current.left)
            else:
                return
        walk(self.root)
        return self.value

    def  breadth_first_traversal(self,rootnode):
        """
        This is breadth_first_traversal method to travesal in the binary tree through
        breadth (level by level).
        Return: a list begin from the root, end up with the last right child in the last level.
        """
        thislevel = [rootnode]
        while thislevel:
            nextlevel = list()
            for n in thislevel:
                print (n.value)
                if n.left: nextlevel.append(n.left)
                if n.right: nextlevel.append(n.right)
            print
            thislevel = nextlevel

class Binary_Search_Tree:
    def __init__(self,root):
        self.root=TNode(root)

    def pre_order(self):
        result=[]
        def walk(current):
            """
            ROOT -> LEFT -> RIGHT.
            """
            if current:
                result.append(str(current.value))
            if current.left:    
                walk(current.left)
            if current.right:
                walk(current.right)
        walk(self.root)
        return result
        


    def in_order(self):
        """
         LEFT-> ROOT -> RIGHT.
        """
        result=[]
        def walk(current):
            if current:
                if current.left:
                    walk(current.left)
                result.append(str(current.value))
                if current.right:
                    walk(current.right)
        walk(self.root)
        return result

    def post_order(self):
        """
          LEFT -->> RIGHT -->> ROOT.
        """
        result=[]
        def walk(current):
            if current:
                if current.left:
                    walk(current.left)
                if current.right:
                    walk(current.right)
                result.append(str(current.value))
        walk(self.root)
        return result

    def add(self,value):
        if not self.root:
            self.root=TNode(value)
        else:
            def addt(current):
                if current.value >= value:
                    if current.left:
                        addt(current.left)
                    else:
                        current.left = TNode(value)
                elif current.value < value:
                    if current.right:
                        addt(current.right)
                    else:
                        current.right = TNode(value)
            addt(self.root)

    def contain(self,value):
        self.flag = False

        def contains(current):
            if current:
                if current.value == value:
                    self.flag = True
 
                if current.value < value:
                    if current.right:
                        contains(current.right)
                    else:
                        self.flag = False

                if current.value > value:   
                    if current.left:
                        contains(current.left)
                    else:
                        self.flag = False
            else:
                self.flag = False
         
        contains(self.root)
        return self.flag

    

    
if __name__ == "__main__":
    
    tree = Binary_Tree(10)
    tree.root.left = TNode(90)
    tree.root.left.left = TNode(27)
    tree.root.left.right = TNode(8)
    tree.root.right = TNode(16)
    tree.root.right.left= TNode(11)
    tree.root.right.right = TNode(97)
    print(tree.find_max())
    print(tree.pre_order())
    print(tree.breadth_first_traversal(tree.root))
    # print("pre_order",tree.call_tv("pre_order"))
    # print("in_order",tree.call_tv("in_order"))
    # print("post_order",tree.call_tv("post_order"))
    # # print("contains 10?", tree.contain(10))
    # test = Binary_Search_Tree(20)
    # test.add(10)
    # test.add(30)
    # test.add(40)
    # test.add(25)
    # test.add(12)
    # print(test.pre_order())
    # print(test.contain(60))