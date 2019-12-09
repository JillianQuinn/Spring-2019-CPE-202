import unittest
from binary_search_tree import *


class TestLab4(unittest.TestCase):

    def test_simple(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        bst.insert(10, 'stuff')
        self.assertTrue(bst.search(10))
        self.assertEqual(bst.find_min(), (10, 'stuff'))
        bst.insert(10, 'other')
        self.assertEqual(bst.find_max(), (10, 'other'))
        self.assertEqual(bst.tree_height(), 0)
        self.assertEqual(bst.inorder_list(), [10])
        self.assertEqual(bst.preorder_list(), [10])
        self.assertEqual(bst.level_order_list(), [10])

    def test_search(self):
        bst = BinarySearchTree()
        bst.insert(1, 'stuff')
        self.assertTrue(bst.search(1))
        bst.insert(3, 'words')
        bst.insert(2, 'data')
        bst.insert(4, 'data')
        bst.insert(7, 'words')
        bst.insert(6, 'data')
        bst.insert(5, 'data')
        self.assertTrue(bst.search(4))
        self.assertTrue(bst.search(2))
        self.assertFalse(bst.search(8))
        self.assertEqual(bst.find_min(), (1, 'stuff'))
        self.assertEqual(bst.find_max(), (7, 'words'))

    def test_height(self):
        """Test a well formed tree of height 3."""
        tree = BinarySearchTree()
        tree.insert(42, 'stuff')
        tree.insert(53, 'words')
        tree.insert(21, 'data')
        tree.insert(35, 'data')
        tree.insert(62, 'words')
        tree.insert(14, 'data')
        tree.insert(28, 'data')
        self.assertTrue(tree.search(42))
        self.assertTrue(tree.search(53))
        self.assertTrue(tree.search(21))
        self.assertTrue(tree.search(35))
        self.assertTrue(tree.search(62))
        self.assertTrue(tree.search(14))
        self.assertTrue(tree.search(28))
        self.assertFalse(tree.search(51))
        self.assertFalse(tree.search(27))
        self.assertEqual(tree.inorder_list(), [14, 21, 28, 35, 42, 53, 62])
        self.assertEqual(tree.preorder_list(), [42, 21, 14, 35, 28, 53, 62])
        self.assertEqual(tree.level_order_list(), [42, 21, 53, 14, 35, 62, 28])
        self.assertEqual(tree.tree_height(), 3)
        """Testing find min max in a well balanced tree"""
        self.assertEqual(tree.find_max(), (62, 'words'))
        self.assertEqual(tree.find_min(), (14, 'data'))
        """Test a well formed tree of height 2."""
        bst = BinarySearchTree()
        bst.insert(5, 'stuff')
        bst.insert(3, 'words')
        bst.insert(2, 'data')
        bst.insert(4, 'data')
        bst.insert(7, 'words')
        bst.insert(6, 'data')
        bst.insert(8, 'data')
        self.assertEqual(bst.tree_height(), 2)
        """test well formed lists"""
        self.assertEqual(bst.inorder_list(), [2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(bst.preorder_list(), [5, 3, 2, 4, 7, 6, 8])
        self.assertEqual(bst.level_order_list(), [5, 3, 7, 2, 4, 6, 8])
        """test an empty tree with max, min, is_empty, tree height, lists, and search"""
        bst2 = BinarySearchTree()
        self.assertTrue(bst2.is_empty())
        self.assertEqual(bst2.tree_height(), None)
        self.assertEqual(bst2.find_max(), None)
        self.assertEqual(bst2.find_min(), None)
        self.assertEqual(bst2.search(2), False)
        self.assertEqual(bst2.inorder_list(), [])
        self.assertEqual(bst2.preorder_list(), [])
        self.assertEqual(bst2.level_order_list(), [])
        """Test a tree with just a root max min and height"""
        bst2.insert(1, 'words')
        self.assertEqual(bst2.tree_height(), 0)
        self.assertEqual(bst2.find_max(), (1, 'words'))
        self.assertEqual(bst2.find_min(), (1, 'words'))
        self.assertEqual(bst2.find_min(), bst2.find_max())
        """Test a tree with a height of 1"""
        bst2.insert(2, 'data')
        """Test a badly formed tree max min and height"""
        bst2.insert(3, 'data')
        bst2.insert(4, 'data')
        bst2.insert(5, 'data')
        bst2.insert(6, 'data')
        bst2.insert(7, 'data')
        self.assertEqual(bst2.inorder_list(), [1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(bst2.tree_height(), 6)
        self.assertEqual(bst2.find_max(), (7, 'data'))
        self.assertEqual(bst2.find_min(), (1, 'words'))


if __name__ == '__main__': 
    unittest.main()
