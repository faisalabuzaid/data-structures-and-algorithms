from code_challenges.tree_intersection.tree_intersection import tree_intersection, BinaryTree, Node

def test_tree_intersection():
    """
    Intersection for two trees.
    """

    tree1 = BinaryTree(150)
    tree1.root.left = Node(100)
    tree1.root.left.left = Node(75)
    tree1.root.left.right = Node(160)
    tree1.root.left.right.left = Node(125)
    tree1.root.left.right.right = Node(175)
    tree1.root.right = Node(250)
    tree1.root.right.left= Node(200)
    tree1.root.right.right = Node(350)
    tree1.root.right.right.left = Node(300)
    tree1.root.right.right.right = Node(500)

    tree = BinaryTree(42)
    tree.root.left = Node(100)
    tree.root.left.left = Node(15)
    tree.root.left.right = Node(160)
    tree.root.left.right.left = Node(125)
    tree.root.left.right.right = Node(175)
    tree.root.right = Node(600)
    tree.root.right.left= Node(200)
    tree.root.right.right = Node(350)
    tree.root.right.right.left = Node(4)
    tree.root.right.right.right = Node(500)

    expected = [100, 160, 125, 175, 200, 350, 500]
    actual = tree_intersection(tree, tree1)
    assert actual == expected