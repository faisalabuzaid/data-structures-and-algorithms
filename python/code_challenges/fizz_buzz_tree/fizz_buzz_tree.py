
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
    def __init__(self):
        self.root=None


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
        result =[]
        while thislevel:
            nextlevel = list()
            for n in thislevel:
                result.append(n.value)
                if n.left: nextlevel.append(n.left)
                if n.right: nextlevel.append(n.right)
            print
            thislevel = nextlevel
        return result

    



def FizzBuzzTree(tree):

    try:
        tree = tree.contains('pre_order')
        if not tree :
            return "The tree is an empty"
        else:
            result = Binary_Tree()
            for i in range(len(tree)):
                if int(tree[i]) % 3 ==0 and int(tree[i]) %5  == 0:
                    result.a('FizzBuzz')
                elif int(tree[i]) % 3 == 0:
                    output.append('Fizz')
                elif int(tree[i]) % 5 == 0:
                    output.append('Buzz')
                else:
                    output.append(tree[i])
            return output
    except Exception as error:
        print(f"There is error in FizzBuzzTree {error}")



if __name__ == "__main__":
    tree = Binary_Tree()
    tree.root = TNode(10)
    print(len(tree))
    # tree.root.left = Node(7)
    # tree.root.left.left = Node(2)
    # tree.root.left.right = Node(6)
    # tree.root.left.right.left = Node(5)
    # tree.root.left.right.right = Node(11)
    # tree.root.right = Node(5)
    # tree.root.right.right= Node(9)
    # tree.root.right.right.left = Node(4)
    # # tree.add(15)
    # # print(tree.add(15))
    # print("pre_order",tree.contains("pre_order"))
    # print("in_order",tree.contains("in_order"))
    # print("post_order",tree.contains("post_order"))

    # print(tree.find_maximum_value(tree.root))
    # print(tree.breadth_first_traversal(tree.root))
    # print(FizzBuzzTree(tree))