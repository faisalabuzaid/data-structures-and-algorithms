class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.right = None
        self.left = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):

        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    def __str__(self) -> str:
        result = ""
        current = self.head
        while current:
            result += f"{str(current.data)}, "
            current = current.next
        return result

class BinaryTree:
    def __init__(self, root = None):
        self.root = Node(root)

    def contains(self, value):
        self.flag = False
        def walk(current):
            if current:
                if current.data == value:
                   self.flag = True
                if current.left:
                    walk(current.left)
                if current.right:
                    walk(current.right)
        walk(self.root)
        return self.flag
        
def tree_intersection(tree_one,tree_two):
    result = LinkedList()
    def walk(current_one, current_two):
        if current_one and current_two.root:
            if current_two.contains(current_one.data):
                result.add(current_one.data)
            if current_one.left:
                walk(current_one.left, current_two)
            if current_one.right:
                walk(current_one.right, current_two)

    walk(tree_one.root, tree_two)
    return result


if __name__ == "__main__":

    tree = BinaryTree(10)
    tree.root.left = Node(90)
    tree.root.left.left = Node(27)
    tree.root.left.right = Node(8)
    tree.root.right = Node(16)
    tree.root.right.left= Node(11)
    tree.root.right.right = Node(97)

    treetwo = BinaryTree(11)
    treetwo.root.left = Node(97)
    treetwo.root.left.left = Node(27)
    treetwo.root.left.right = Node(8)
    treetwo.root.right = Node(16)
    treetwo.root.right.left= Node(11)
    treetwo.root.right.right = Node(99)
    print(tree_intersection(tree,treetwo))
