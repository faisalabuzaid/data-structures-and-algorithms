from typing import Counter


class Node:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None
    
class Binary_Tree:
    def __init__(self,root):
        self.root=Node(root)


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
            self.root = Node(value)
        else:
            # current=self.root
            def addt(current):

                if value >= current.value:
                    if current.right:
                        addt(current.right)
                    else:
                        current.right = Node(value)

                    
                elif value < current.value:
                    if current.left:
                        addt(current.left)
                    else:
                        current.left = Node(value)

            addt(self.root)

    def contain(self,value):
        def contains(current):
            if current:
                print(current.value)
                if current.value == value:
                    print('True')
                    return True
                elif current.value < value:
                    if current.right:
                        contains(current.right)
                    else:
                        return False

                elif current.value > value:
                    if current.left:
                        contains(current.left)
                    else:
                        return False
        
        test = contains(self.root)
        print(test)
        return test

    
if __name__ == "__main__":
    # tree = Binary_Tree(1)
    # tree.root.left = Node(2)
    # tree.root.right = Node(3)
    # tree.root.right.left= Node(4)
    # tree.root.right.right = Node(5)

    bst = Binary_Tree(20)
    bst.add(10)
    print(bst.root.left)
    # bst.add(30)
    # bst.add(5)
    # bst.add(40)
    # bst.add(50)
    # print(bst.root.left.value)
    print("pre_order",bst.pre_order())

    # print(bst.root.right.value)
    print("contains 10?", bst.contain(10))

    # print('bst', bst.right.value)

    # print("pre_order",tree.pre_order())
    # print("in_order",tree.in_order())
    # print("post_order",tree.post_order())
    # print("contains 10?", tree.contain(0))