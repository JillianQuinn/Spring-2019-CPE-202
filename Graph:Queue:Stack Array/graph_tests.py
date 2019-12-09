import unittest
from graph import *


class TestList(unittest.TestCase):

    def test_01(self):
        """Test file 1 with two connected components"""
        g = Graph('test1.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5'], ['v6', 'v7', 'v8', 'v9']])
        self.assertTrue(g.is_bipartite())
        
    def test_02(self):
        """Test file 2 with two connected components"""
        g = Graph('test2.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3'], ['v4', 'v6', 'v7', 'v8']])
        self.assertFalse(g.is_bipartite())

    def test_03(self):
        """Test file 3 with 4 connected components"""
        g = Graph('test3.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v100'], ['v2', 'v3'], ['v5', 'v6'], ['v10', 'v11']])
        self.assertTrue(g.is_bipartite())

    def test_04(self):
        """Test file 4 with 1 connected component """
        g = Graph('test4.txt')
        self.assertEqual(g.conn_components(), [['v5', 'v6']])
        self.assertTrue(g.is_bipartite())

    def test_05(self):
        """Test file 5 with empty file"""
        g = Graph('test5.txt')
        self.assertEqual(g.conn_components(), [['1', '12', '13'], ['10', '2', '3', '5', '6', '7', '8'], ['11', '4', '9']])
        self.assertFalse(g.is_bipartite())

    def test_06(self):
        """Test file 6 with 1 long component"""
        g = Graph('test6.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5']])
        self.assertFalse(g.is_bipartite())

    def test_07(self):
        """Test file 7 a larger graph"""
        g = Graph('test7.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v10', 'v11', 'v12', 'v13', 'v14', 'v15', 'v16', 'v17', 'v18','v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'v9']])
        self.assertTrue(g.is_bipartite())

    def test_08(self):
        """Test file 8 a cycle"""
        g = Graph('test8.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2']])
        self.assertTrue(g.is_bipartite())

    def test_09(self):
        """Test file 9 a cycle"""
        g = Graph('test9.txt')
        self.assertEqual(g.conn_components(), [['1', '2', '3', '4', '5', '6', '7', '8', '9']])
        self.assertFalse(g.is_bipartite())

    def test_10(self):
        """Test file 9 a cycle"""
        g = Graph('test10.txt')
        self.assertEqual(g.conn_components(), [['1', '2', '3', '4']])
        self.assertFalse(g.is_bipartite())


    def test_11(self):
        """Test file 9 a cycle"""
        g = Graph('test11.txt')
        self.assertEqual(g.conn_components(), [['1', '10', '11', '2', '3', '4', '5', '6', '7', '8', '9']])
        self.assertFalse(g.is_bipartite())


if __name__ == '__main__':
   unittest.main()
