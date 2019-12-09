import unittest
import filecmp
from concordance import *


class TestList(unittest.TestCase):

    def test_01(self):
        # Test file 1
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("file1.txt")
        conc.write_concordance("file1_con.txt")
        self.assertTrue(filecmp.cmp("file1_con.txt", "file1_sol.txt"))

    def test_02(self):
        # Test file 2
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("file2.txt")
        conc.write_concordance("file2_con.txt")
        self.assertTrue(filecmp.cmp("file2_con.txt", "file2_sol.txt"))

    def test_03(self):
        # test declaration
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("declaration.txt")
        conc.write_concordance("declaration_con.txt")
        self.assertTrue(filecmp.cmp("declaration_con.txt", "declaration_sol.txt"))

    def test_empty(self):
        # Test empty file
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("empty.txt")
        conc.write_concordance("empty_con.txt")
        self.assertTrue(filecmp.cmp("empty_con.txt", "empty_sol.txt"))

    def test_punc(self):
        # Test punctuation
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("punct.txt")
        conc.write_concordance("punct_con.txt")

    def test_FNF(self):
        # Test file not found error
        conc = Concordance()
        with self.assertRaises(FileNotFoundError):
            conc.load_stop_table("random_file.txt")
        self.assertRaises(FileNotFoundError, conc.load_concordance_table, "file_not_here.txt")
        self.assertRaises(FileNotFoundError, conc.load_concordance_table, "")

    def test_stop(self):
        # running the stop file should be an empty file
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("stop_words.txt")
        conc.write_concordance("stop_file_con.txt")
        self.assertTrue(conc.stop_table.in_table("on"), True)
        self.assertTrue(filecmp.cmp("stop_file_con.txt", "empty_sol.txt"))

    def test_dict(self):
        """Test dictionary"""
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("dict.txt")
        conc.write_concordance("dict_con.txt")

    def test_wap(self):
        """Testing war and peace"""
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("wap.txt")
        conc.write_concordance("wap_con.txt")

    def test_repeated(self):
        # test a repeated word
        conc = Concordance()
        conc.load_stop_table("stop_file_the.txt")
        conc.load_concordance_table("repeated.txt")
        conc.write_concordance("repeated_con.txt")
        self.assertTrue(filecmp.cmp("repeated_con.txt", "repeated_sol.txt"))

    def test_spaces(self):
        # test a repeated word
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("spacing.txt")
        conc.write_concordance("spacing_con.txt")
        self.assertTrue(filecmp.cmp("spacing_con.txt", "spacing_sol.txt"))


if __name__ == '__main__':
    unittest.main()
