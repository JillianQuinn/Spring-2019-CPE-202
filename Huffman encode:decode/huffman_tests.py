import unittest
import filecmp
import subprocess
from huffman import *


class TestList(unittest.TestCase):
    def test_comes_before(self):
        """test to make sure the comes before selects the correct values"""
        self.assertTrue(comes_before(HuffmanNode(30, 15), HuffmanNode(32, 15)))
        self.assertFalse(comes_before(HuffmanNode(30, 20), HuffmanNode(32, 15)))
        self.assertFalse(comes_before(HuffmanNode(96, 15), HuffmanNode(90, 15)))
        self.assertTrue(comes_before(HuffmanNode(96, 2), HuffmanNode(100, 23)))

    def test_combine(self):
        """tests implementation of combining two nodes"""
        a = HuffmanNode(90, 2)
        b = HuffmanNode(96, 5)
        node = combine(a, b)
        self.assertTrue(node.freq == 7)
        self.assertTrue(node.char == a.char)
        self.assertTrue(node.left == a)
        self.assertTrue(node.right == b)

    def test_cnt_freq(self):
        """Verifies that it counts correctly, and that file not found error works"""
        freqlist	= cnt_freq("file2.txt")
        anslist = [2, 4, 8, 16, 0, 2, 0]
        self.assertListEqual(freqlist[97:104], anslist)
        with self.assertRaises(FileNotFoundError):
            freqlist = cnt_freq("fdsafa.txt")

    def test_create_huff_tree(self):
        """Tets huff tree implementation"""
        lst = []
        self.assertTrue(create_huff_tree(lst) is None)
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        self.assertEqual(hufftree.freq, 32)
        self.assertEqual(hufftree.char, 97)
        left = hufftree.left
        self.assertEqual(left.freq, 16)
        self.assertEqual(left.char, 97)
        right = hufftree.right
        self.assertEqual(right.freq, 16)
        self.assertEqual(right.char, 100)
        listt = [4]
        node = create_huff_tree(listt)
        self.assertTrue(node.char == 0)
        self.assertTrue(node.freq == 4)

    def test_create_header(self):
        """Verifies header creation"""
        freqlist = cnt_freq("file2.txt")
        self.assertEqual(create_header(freqlist), "97 2 98 4 99 8 100 16 102 2")
        freqlist = [0, 1500]
        self.assertEqual(create_header(freqlist), "1 1500")

    def test_create_code(self):
        """checks create code for file 1 and 2 and multiline"""
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord('d')], '1')
        self.assertEqual(codes[ord('a')], '0000')
        self.assertEqual(codes[ord('f')], '0001')

        freqlist = cnt_freq("file1.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord('a')], '11')
        self.assertEqual(codes[ord('b')], '01')
        self.assertEqual(codes[ord('c')], '101')
        self.assertEqual(codes[ord('d')], '100')
        self.assertEqual(codes[ord(' ')], '00')

        freqlist = cnt_freq("multiline.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord('\n')], '00101')
        self.assertEqual(codes[ord(' ')], '101')

    def test_01_textfile(self):
        """full text1 implementation"""
        huffman_encode("file1.txt", "file1_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb file1_out.txt file1_soln.txt", shell = True)
        self.assertEqual(err, 0)
        err = subprocess.call("diff -wb file1_out_compressed.txt file1_compressed_soln.txt", shell = True)
        self.assertEqual(err, 0)

    def test_02_textfile(self):
        """full text2 implementation"""
        huffman_encode("file2.txt", "file2_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb file2_out.txt file2_soln.txt", shell = True)
        self.assertEqual(err, 0)
        err = subprocess.call("diff -wb file2_out_compressed.txt file2_compressed_soln.txt", shell = True)
        self.assertEqual(err, 0)

    def test_1_chr(self):
        """1 chr implementation"""
        huffman_encode("1_chr.txt", "1_chr_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb 1_chr_out.txt 1_chr_out_soln.txt", shell = True)
        self.assertEqual(err, 0)
        err = subprocess.call("diff -wb 1_chr_out_compressed.txt 1_chr_out_compressed_soln.txt", shell = True)
        self.assertEqual(err, 0)

    def test_1_space(self):
        """1 space implementation"""
        huffman_encode("1_space.txt", "1_space_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb 1_space_out.txt 1_space_out_soln.txt", shell=True)
        self.assertEqual(err, 0)
        err = subprocess.call("diff -wb 1_space_out_compressed.txt 1_space_out_compressed_soln.txt", shell=True)
        self.assertEqual(err, 0)

    def test_alternating(self):
        """alternating characters and empty lines implementation"""
        huffman_encode("alternating.txt", "alternating_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb alternating_out.txt alternating_out_soln.txt", shell=True)
        self.assertEqual(err, 0)
        err = subprocess.call("diff -wb alternating_out_compressed.txt alternating_out_compressed_soln.txt", shell=True)
        self.assertEqual(err, 0)

    def test_repeated_chr(self):
        """repeated character implementation"""
        huffman_encode("repeated.txt", "repeated_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb repeated_out.txt repeated_out_soln.txt", shell = True)
        self.assertEqual(err, 0)
        err = subprocess.call("diff -wb repeated_out_compressed.txt repeated_out_compressed_soln.txt", shell = True)
        self.assertEqual(err, 0)

    def test_empty_textfile(self):
        """full empty file implementation"""
        huffman_encode("empty_file.txt", "empty_file_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb empty_file_out.txt empty_file.txt", shell=True)
        self.assertEqual(err, 0)
        err = subprocess.call("diff -wb empty_file_out_compressed.txt empty_file.txt", shell=True)
        self.assertEqual(err, 0)

    def test_declaration_textfile(self):
        """full delcaration implementation"""
        huffman_encode("declaration.txt", "declaration_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb declaration_out.txt declaration_soln.txt", shell=True)
        self.assertEqual(err, 0)
        err = subprocess.call("diff -wb declaration_out_compressed.txt declaration_compressed_soln.txt", shell=True)
        self.assertEqual(err, 0)

    def test_multiline_textfile(self):
        """full multiline implementation"""
        huffman_encode("multiline.txt", "multiline_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb multiline_out.txt multiline_soln.txt", shell=True)
        self.assertEqual(err, 0)
        err = subprocess.call("diff -wb multiline_out_compressed.txt multiline_compressed_soln.txt", shell=True)
        self.assertEqual(err, 0)

    """def test_wap(self):
        huffman_encode("wap.txt", "wap_out.txt")
    # capture errors by running 'diff' on your encoded file with a *known* solution file"""

    def test_no_file(self):
        """file not found"""
        with self.assertRaises(FileNotFoundError):
            huffman_encode("multi.txt", "multi_out.txt")
        self.assertRaises(FileNotFoundError, huffman_encode, "file_not_here.txt", "")
        self.assertRaises(FileNotFoundError, huffman_encode, "file_not_heretxt", "hellotext")

    def test_parse_header(self):
        self.assertEqual(parse_header("0 12 1 3 4 1 6 2 7 8")[:8], [12, 3, 0, 0, 1, 0, 2, 8])

    def test_huffman_decode(self):
        """File 1"""
        huffman_decode("file1_compressed_soln.txt", "file1_decode.txt", )
        err = subprocess.call("diff -wb file1_decode.txt file1.txt", shell=True)

        """file 2"""
        huffman_decode("file2_compressed_soln.txt", "file2_decode.txt", )
        err = subprocess.call("diff -wb file2_decode.txt file2.txt", shell=True)

        """declaration"""
        huffman_decode("declaration_compressed_soln.txt", "declaration_decode.txt", )
        err = subprocess.call("diff -wb declaration_decode.txt declaration.txt", shell=True)

        """multiline"""
        huffman_decode("multiline_compressed_soln.txt", "multiline_decode.txt", )
        err = subprocess.call("diff -wb multiline_decode.txt multiline.txt", shell=True)

        """1 character"""
        huffman_decode("1_chr_out_compressed_soln.txt", "1_chr_decode.txt", )
        err = subprocess.call("diff -wb 1_chr_decode.txt 1_chr.txt", shell=True)

        """repeated character"""
        huffman_decode("repeated_out_compressed_soln.txt", "repeated_decode.txt", )
        err = subprocess.call("diff -wb repeated_decode.txt repeated.txt", shell=True)

        """empty file"""
        huffman_decode("empty_file_compressed_soln.txt", "empty_file_decode.txt", )
        err = subprocess.call("diff -wb empty_file_decode.txt empty_file.txt", shell=True)

        """file not found error"""
        with self.assertRaises(FileNotFoundError):
            huffman_decode("nope_compressed.txt", "nope_out.txt")
        self.assertRaises(FileNotFoundError, huffman_decode, "file_not_here.txt", "")
        self.assertRaises(FileNotFoundError, huffman_decode, "file_not_heretxt", "hellotext")

        """testing alternating characters, empty line, space, and multiline"""
        huffman_decode("alternating_out_compressed_soln.txt", "alternating_decode.txt", )
        err = subprocess.call("diff -wb alternating_decode.txt alternating.txt", shell=True)

        """testing file with one space"""
        huffman_decode("1_space_out_compressed_soln.txt", "1_space_decode.txt", )
        err = subprocess.call("diff -wb 1_space_decode.txt 1_space.txt", shell=True)

        """Testing war and peace
        huffman_decode("WAP_out_compressed.txt", "WAP_decode.txt", )
        err = subprocess.call("diff -wb WAP_decode.txt wap.txt", shell=True)"""

    def test_01a_test_file1_parse_header(self):
        f = open('file1_compressed_soln.txt', 'rb')
        header = f.readline()
        f.close()
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0]
        self.compare_freq_counts(parse_header(header), expected)

    def test_01_test_file1_decode(self):
        huffman_decode("file1_compressed_soln.txt", "file1_decoded.txt")
        err = subprocess.call("diff -wb file1.txt file1_decoded.txt", shell=True)
        self.assertEqual(err, 0)

    def compare_freq_counts(self, freq, exp):
        for i in range(256):
            stu = 'Frequency for ASCII ' + str(i) + ': ' + str(freq[i])
            ins = 'Frequency for ASCII ' + str(i) + ': ' + str(exp[i])
            self.assertEqual(stu, ins)


if __name__ == '__main__':
    unittest.main()

