class Node:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None
    
class Binary_Tree:
    def __init__(self,root):
        self.root=Node(root)

    def pre_order(self,current,v_list):
        """
         ROOT -> LEFT -> RIGHT.
        """
        try:
            if current:
                v_list.append(str(current.value))
                v_list = self.pre_order(current.left, v_list)
                v_list = self.pre_order(current.right, v_list)
            return v_list
        except Exception as error:
            print(f"There is error in pre-order:{error}")
        


    def in_order(self,current,v_list):
        """
         LEFT-> ROOT -> RIGHT.
        """
        try:
            if current:
                v_list = self.in_order(current.left,v_list)
                v_list.append(str(current.value))
                v_list = self.in_order(current.right,v_list)
            return v_list
        except Exception as error:
            print(f"There is error in in_order:{error}")

    def post_order(self,current,v_list):
        """
          LEFT -->> RIGHT -->> ROOT.
        """
        try:
            if current:
                v_list = self.post_order(current.left,v_list)
                v_list = self.post_order(current.right,v_list)
                v_list.append(str(current.value))
            return v_list
        except Exception as error:
            print(f"There is error in post_order:{error}")

    def add(self,value):
        try:
            if not self.root:
                self.root=Node(value)
            else:
                new_node=Node(value)
                if new_node>=self.root:
                    self.root.right=new_node
                    return self.root.right
                elif new_node<self.root:
                    self.root.left=new_node
                    return self.root.left
        except Exception as error:
            print(f"There is error in add:{error}")

    def contain(self,value):
        current = self.root
        def contains(current=current,value=value):
            try:
                if current:
                    if current.value == value:
                        return True
                    elif current.value > value:
                        current = current.left
                        contains(current,value)
                    elif current.value < value:
                        current = current.right
                        contains(current,value)
                else:
                    return False 
            except Exception as error:
                print(f"There is error in call_tv :{error}")

    def call_tv (self,type_depth):
        try:
            if type_depth == "pre_order":
                return self.pre_order(self.root,[])
            elif type_depth == "in_order":
                return self.in_order(self.root,[])
            elif type_depth == "post_order":
                return self.post_order(self.root,[])
            else:
                print("Wrong type depth")
                return False 
        except Exception as error:
            print(f"There is error in call_tv :{error}")
    
if __name__ == "__main__":
    tree = Binary_Tree(10)
    tree.root.left = Node(9)
    tree.root.left.left = Node(7)
    tree.root.left.right = Node(8)
    tree.root.right = Node(16)
    tree.root.right.left= Node(11)
    tree.root.right.right = Node(17)

    print("pre_order",tree.call_tv("pre_order"))
    print("in_order",tree.call_tv("in_order"))
    print("post_order",tree.call_tv("post_order"))
    print("contains 10?", tree.contain(10))