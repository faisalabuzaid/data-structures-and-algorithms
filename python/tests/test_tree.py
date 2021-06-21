# from code_challenges.tree.tree import Node, TNode, Binary_Tree, Binary_Search_Tree
# import pytest

# def test_pre_order():
#     tree = Binary_Tree(10)
#     tree.root.left = TNode(9)
#     tree.root.left.left = TNode(7)
#     tree.root.left.right = TNode(8)
#     tree.root.right = TNode(16)
#     tree.root.right.left= TNode(11)
#     tree.root.right.right = TNode(17)
#     expected = ['10', '9', '7', '8', '16', '11', '17']
#     actual = tree.pre_order()
#     assert actual == expected

# def test_in_order():
#     tree = Binary_Tree(10)
#     tree.root.left = TNode(9)
#     tree.root.left.left = TNode(7)
#     tree.root.left.right = TNode(8)
#     tree.root.right = TNode(16)
#     tree.root.right.left= TNode(11)
#     tree.root.right.right = TNode(17)
#     actual = tree.in_order()
#     expected = ['7', '9', '8', '10', '11', '16', '17' ]
#     assert actual == expected

# def test_post_order():
#     tree = Binary_Tree(10)
#     tree.root.left = TNode(9)
#     tree.root.left.left = TNode(7)
#     tree.root.left.right = TNode(8)
#     tree.root.right = TNode(16)
#     tree.root.right.left= TNode(11)
#     tree.root.right.right = TNode(17)
#     actual = tree.post_order()
#     expected = ['7', '8', '9', '11', '17', '16', '10' ]
#     assert actual == expected

# def test_add():
#     test = Binary_Search_Tree(20)
#     test.add(10)
#     test.add(30)
#     test.add(40)
#     test.add(25)
#     test.add(12)
#     actual = test.pre_order()
#     expected = ['20', '10', '12', '30', '25', '40']
#     assert actual == expected

# def test_contain():
#     test = Binary_Search_Tree(20)
#     test.add(10)
#     test.add(30)
#     test.add(40)
#     test.add(25)
#     test.add(12)
#     actual_1 = test.contain(10)
#     actual_2 = test.contain(20)
#     actual_3 = test.contain(60)

#     expected_1 = True
#     expected_2 = True
#     expected_3 = False
#     assert actual_1 == expected_1
#     assert actual_2 == expected_2
#     assert actual_3 == expected_3

# def test_find_max():
#     tree = Binary_Tree(10)
#     tree.root.left = TNode(90)
#     tree.root.left.left = TNode(27)
#     tree.root.left.right = TNode(8)
#     tree.root.right = TNode(16)
#     tree.root.right.left= TNode(11)
#     tree.root.right.right = TNode(87)
#     actual = tree.find_max()
#     false_expected = 87
#     expected = 90
#     assert actual == expected
#     assert actual != false_expected

# def test_breadth_first():
#     tree = Binary_Tree(10)
#     tree.root.left = TNode(90)
#     tree.root.left.left = TNode(27)
#     tree.root.left.right = TNode(8)
#     tree.root.right = TNode(16)
#     tree.root.right.left= TNode(11)
#     tree.root.right.right = TNode(97)
#     actual = tree.breadth_first_traversal(tree.root)
#     expected = [10, 90, 16, 27, 8, 11, 97]
#     assert actual == expected
