import unittest
from hash_quad import *

class TestList(unittest.TestCase):

    def test_01a(self):
        """get table size one item original"""
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_table_size(), 7)

    def test_01b(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_num_items(), 1)
        """testing add same value that you have the same num items"""
        ht.insert("cat", 5)
        self.assertEqual(ht.get_num_items(), 1)
        """testing adding different values and num items increases"""
        ht.insert("dog", 1)
        self.assertEqual(ht.get_num_items(), 2)
        ht.insert("d", 2)
        ht.insert("o", 3)
        self.assertEqual(ht.get_num_items(), 4)

    def test_01c(self):
        """testing load factor"""
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertAlmostEqual(ht.get_load_factor(), 1/7)

    def test_01d(self):
        ht = HashTable(7)
        """test get all keys empty list"""
        self.assertEqual(ht.get_all_keys(), [])
        """Test get all keys for one item"""
        ht.insert("cat", 5)
        self.assertEqual(ht.get_all_keys(), ["cat"])
        ht.insert("dog", 5)
        ht.insert("fish", 5)
        ht.insert("zebra", 5)
        ht.insert("monkey", 5)
        """test get all keys multiple items"""
        self.assertEqual(ht.get_all_keys(), ['monkey', 'fish', 'zebra', 'cat', 'dog'])

    def test_01e(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        """Check for value in list"""
        self.assertEqual(ht.in_table("cat"), True)
        ht.insert("zebra", 5)
        ht.insert("monkey", 5)
        """check with more values in the list"""
        self.assertEqual(ht.in_table("monkey"), True)
        """check value not in list"""
        self.assertEqual(ht.in_table("elephant"), False)

    def test_01f(self):
        """test get value"""
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_value("cat"), 5)
        ht.insert("cat", 8)
        """test updating values"""
        self.assertEqual(ht.get_value("cat"), 8)
        ht.insert("zebra", 18)
        """test multiple values in hash"""
        self.assertEqual(ht.get_value("zebra"), 18)

    def test_01g(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        """testing get index"""
        self.assertEqual(ht.get_index("cat"), 3)
        ht.insert("cat", 15)
        """testing updating the value keeps index"""
        self.assertEqual(ht.get_index("cat"), 3)
        ht.insert("fish", 3)
        ht.insert("zebra", 2)
        ht.insert("monkey", 1)
        """test get index of multiple items"""
        self.assertEqual(ht.get_index("fish"), 6)
        self.assertEqual(ht.get_index("zebra"), 7)
        self.assertEqual(ht.get_index("monkey"), 14)
        """not in hash"""
        self.assertEqual(ht.get_index("pig"), None)
        self.assertEqual(ht.get_value("pig"), None)


if __name__ == '__main__':
   unittest.main()
