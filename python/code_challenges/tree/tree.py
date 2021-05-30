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




class Binary_Search_Tree:
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
            self.root=Node(value)
        else:
            def addt(current):
                if current.value >= value:
                    if current.left:
                        addt(current.left)
                    else:
                        current.left = Node(value)
                elif current.value < value:
                    if current.right:
                        addt(current.right)
                    else:
                        current.right = Node(value)
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
    tree.root.left = Node(90)
    tree.root.left.left = Node(27)
    tree.root.left.right = Node(8)
    tree.root.right = Node(16)
    tree.root.right.left= Node(11)
    tree.root.right.right = Node(97)
    print(tree.find_max())
    print(tree.pre_order())

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