from hash_quad import *
import string


class Concordance:

    def __init__(self):
        self.stop_table = None          # hash table for stop words
        self.concordance_table = None   # hash table for concordance

    def load_stop_table(self, filename):
        """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
        Starting size of hash table should be 191: self.stop_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        try:
            fp = open(filename, "r")
            line = fp.readline()
            self.stop_table = HashTable(191)
            while line:
                line = line.strip()
                self.stop_table.insert(line)
                line = fp.readline()
            fp.close()
        except FileNotFoundError:
            raise FileNotFoundError

    def load_concordance_table(self, filename):
        """ Read words from input text file (filename) and insert them into the concordance hash table, 
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)
        Starting size of hash table should be 191: self.concordance_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        try:
            self.concordance_table = HashTable(191)
            conc = open(filename, "r")
            line_num = 0
            line = conc.readline()
            while line:
                line_num += 1
                line = line.replace("'", "")
                line = line.strip()
                line = line.lower()
                no_string = line.maketrans(string.punctuation, ' ' * len(string.punctuation))
                no_digit = line.maketrans(string.digits, ' ' * len(string.digits))
                line = line.translate(no_string)
                line = line.translate(no_digit)
                lst = line.split(" ")
                lst = set(lst)
                lst = list(lst)
                for word in lst:
                    value = self.concordance_table.get_value(word)
                    if value is not None and str(line_num) not in value:
                        self.concordance_table.insert(word, str(value) + " " + str(line_num))
                    elif word != "" and value is None and not self.stop_table.in_table(word):
                        self.concordance_table.insert(word, str(line_num))
                line = conc.readline()
            conc.close()
        except FileNotFoundError:
            raise FileNotFoundError

    def write_concordance(self, filename):
        """ Write the concordance entries to the output file(filename)
        See sample output files for format."""
        file = open(filename, "w")
        lst = self.concordance_table.get_all_keys()
        lst.sort()
        for i in lst:
            value = self.concordance_table.get_value(i)
            if value is not None:
                file.write("{0}: {1}".format(i, "".join(value)))
            if i != lst[len(lst) - 1]:
                file.write("\n")
        file.close()
