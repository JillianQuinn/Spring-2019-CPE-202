from huffman_bit_writer import HuffmanBitWriter
from huffman_bit_reader import HuffmanBitReader


class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char   # stored as an integer - the ASCII character code value
        self.freq = freq   # the freqency associated with the node
        self.left = None   # Huffman tree (node) to the left
        self.right = None  # Huffman tree (node) to the right

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node

    def __lt__(self, other):
        return comes_before(self, other)


def comes_before(a, b):
    """Returns True if tree rooted at node a comes before tree rooted at node b, False otherwise"""
    if a.freq == b.freq:
        return a.char < b.char
    return a.freq < b.freq


def combine(a, b):
    """Creates and returns a new Huffman node with children a and b, with the "lesser node" on the left
    The new node's frequency value will be the sum of the a and b frequencies
    The new node's char value will be the lesser of the a and b char ASCII values"""
    node = HuffmanNode(min(a.char, b.char), a.freq + b.freq)
    if comes_before(a, b):
        node.set_left(a)
        node.set_right(b)
    return node


def cnt_freq(filename):
    """Opens a text file with a given file name (passed as a string) and counts the 
    frequency of occurrences of all the characters within that file"""
    freq_list = [0] * 256
    fp = open(filename, "r")
    lines = fp.readlines()
    fp.close()
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            freq_list[ord(lines[i][j])] += 1
    return freq_list


def create_huff_tree(char_freq):
    """Create a Huffman tree for characters with non-zero frequency
    Returns the root node of the Huffman tree"""
    freq = []
    for i in range(len(char_freq)):
        if char_freq[i] != 0:
            freq.append(HuffmanNode(i, char_freq[i]))
    if len(freq) == 0:
        return None
    freq.sort()
    while len(freq) > 1:
        a = freq.pop(0)
        b = freq.pop(0)
        node = combine(a, b)
        freq.append(node)
        freq.sort()
    return freq[0]


def create_code(node):
    """Returns an array (Python list) of Huffman codes. For each character, use the integer ASCII representation 
    as the index into the arrary, with the resulting Huffman code for that character stored at that location"""
    str_list = [""] * 256
    code = ""
    create_helper(node, str_list, code)
    return str_list


def create_helper(node, lst, code):
    """recursively adds items to the list going through each branch"""
    if node.left is not None:
        create_helper(node.left, lst, code + "0")
    if node.right is not None:
        create_helper(node.right, lst, code + "1")
    else:
        lst[node.char] = code


def create_header(freqs):
    """Input is the list of frequencies. Creates and returns a header for the output file
    Example: For the frequency list asscoaied with "aaabbbbcc, would return “97 3 98 4 99 2” """
    freq_str = ""
    for i in range(len(freqs)):
        if freqs[i] != 0:
            freq_str += "{0} {1} ".format(i, freqs[i])
    return freq_str[:len(freq_str) - 1]


def huffman_encode(in_file, out_file):
    """Takes inout file name and output file name as parameters - both files will have .txt extensions
    Uses the Huffman coding process on the text from the input file and writes encoded text to output file
    Also creates a second output file which adds _compressed before the .txt extension to the name of the file.
    This second file is actually compressed by writing individual 0 and 1 bits to the file using the utility methods 
    provided in the huffman_bits_io module to write both the header and bits.
    Take note of special cases - empty file and file with only one unique character"""
    period = 0
    try:
        if out_file == "" or in_file == "":
            raise FileNotFoundError
        if "." not in out_file or "." not in out_file:
            raise FileNotFoundError
        period = out_file.index(".")
        compressed = out_file[:period] + "_compressed" + out_file[period:]
        compressed = HuffmanBitWriter(compressed)
        freq = cnt_freq(in_file)
        header = create_header(freq)
        node = create_huff_tree(freq)
        encode = ""
        i_f = open(in_file, "r")
        lines = i_f.readlines()
        i_f.close()
        if node is not None:
            code = create_code(node)
            for i in lines:
                for j in i:
                    encode += code[ord(j)]
        if header != "":
            compressed.write_str(header + "\n")
            compressed.write_code(encode)
            o_f = open(out_file, "w")
            o_f.write(header + "\n")
            o_f.write(encode)
            o_f.close()
        compressed.close()
    except FileNotFoundError:
        if period > 0:
            compressed.close()
        raise FileNotFoundError


def huffman_decode(encoded_file, decode_file):
    """reads an encoded textfile, encoded_file,and writes the decoded text into an output text file,
    decode_file,using the Huffman Tree produced by usingthe header information.  If the encoded_file does
    not exist, your program should raise the FileNotFoundError exception. If the specified output file
    already exists, its old contents will be overwritten."""
    """ARRAY IMPLEMENTATION
    decode_open = False
    encode_open = False
    try:
        if encoded_file == "" or decode_file == "":
            raise FileNotFoundError
        decode_file = HuffmanBitWriter(decode_file)
        decode_open = True
        encoded_file = HuffmanBitReader(encoded_file)
        encode_open = True
        header_string = encoded_file.read_str()
        header_list = parse_header(header_string)
        tree = create_huff_tree(header_list)
        body = ""
        if tree is not None:
            code = create_code(tree)
            chars = 0
            num_chars = 0
            for i in header_list:
                chars += i
                if i != 0:
                    num_chars += 1
            if tree.left is None and tree.right is None:
                body += str(chr(tree.char)) * tree.freq
            else:
                for i in range(chars):
                    char = ""
                    if encoded_file.read_bit():
                        char = "1"
                    else:
                        char = "0"
                    while char not in code:
                        if encoded_file.read_bit():
                            char += "1"
                        else:
                            char += "0"
                    body += chr(code.index(char))
            decode_file.write_str(body)
        decode_file.close()
        encoded_file.close()
    except FileNotFoundError:
        if decode_open:
            decode_file.close()
        if encode_open:
            encoded_file.close()
        raise FileNotFoundError"""
    """TREE IMPLEMENTATION"""
    decode_open = False
    encode_open = False
    try:
        if encoded_file == "" or decode_file == "":
            raise FileNotFoundError
        decode_file = HuffmanBitWriter(decode_file)
        decode_open = True
        encoded_file = HuffmanBitReader(encoded_file)
        encode_open = True
        header_string = encoded_file.read_str()
        header_list = parse_header(header_string)
        tree = create_huff_tree(header_list)
        body = ""
        if tree is not None:
            chars = 0
            for i in header_list:
                chars += i
            if tree.left is None and tree.right is None:
                body += str(chr(tree.char)) * tree.freq
            else:
                for i in range(chars):
                    current = tree
                    while current.left is not None and current.right is not None:
                        if encoded_file.read_bit():
                            current = current.right
                        else:
                            current = current.left
                    body += chr(current.char)
            decode_file.write_str(body)
        decode_file.close()
        encoded_file.close()
    except FileNotFoundError:
        if decode_open:
            decode_file.close()
        raise FileNotFoundError


def parse_header(header_string):
    """takes in input header string and returns Python list (array) of frequencies (256 entry list,
    indexed by ASCII value of character)"""
    freq_list = [0] * 256
    freqs = header_string.split()
    for i in range(0, len(freqs), 2):
        freq_list[int(freqs[i])] = int(freqs[i + 1])
    return freq_list
