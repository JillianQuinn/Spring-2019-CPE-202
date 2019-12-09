class HashTable:

    def __init__(self, table_size):         # can add additional attributes
        self.table_size = table_size        # initial table size
        self.hash_table = [None]*table_size # hash table
        self.num_items = 0                  # empty hash table
        self.values = [None] * table_size

    def insert(self, key, value=None):
        """Inserts an entry into the hash table (using Horner hash function to determine index,
        and quadratic probing to resolve collisions).
        The key is a string (a word) to be entered, and value is any object (e.g. Python List).
        If the key is not already in the table, the key is inserted along with the associated value
        If the key is is in the table, the new value replaces the existing value.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased (doubled + 1)."""
        horn = self.horner_hash(key)
        if not self.in_table(key):
            self.hash_table[horn] = key
            self.num_items += 1
        else:
            horn = self.get_index(key)
        self.values[horn] = value
        if self.get_load_factor() > 0.5:
            new = HashTable(self.table_size * 2 + 1)
            for i in range(self.table_size):
                if self.hash_table[i] is not None:
                    new.insert(self.hash_table[i], self.values[i])
            self.table_size = new.table_size
            self.hash_table = new.hash_table
            self.values = new.values

    def horner_hash(self, key):
        """Compute and return an integer from 0 to the (size of the hash table) - 1
        Compute the hash value by using Horner’s rule, as described in project specification."""
        n = min(len(key), 8)
        horn = 0
        for i in range(n):
            horn += ord(key[i]) * (31 ** (n - 1 - i))
        horn = index = horn % self.table_size
        quad = 1
        while self.hash_table[index] is not None and self.hash_table[index] != key:
            index = horn + quad ** 2
            quad += 1
            if index >= self.table_size:
                index = index % self.table_size
        return index

    def in_table(self, key):
        """Returns True if key is in an entry of the hash table, False otherwise."""
        return self.get_index(key) is not None

    def get_index(self, key):
        index = self.horner_hash(key)
        if self.hash_table[index] == key:
            return index
        return None

    def get_all_keys(self):
        """Returns a Python list of all keys in the hash table."""
        key_lst = []
        for i in range(self.table_size):
            if self.hash_table[i] is not None:
                key_lst.append(self.hash_table[i])
        return key_lst

    def get_value(self, key):
        """Returns the value associated with the key.
        If key is not in hash table, returns None."""
        i = self.get_index(key)
        if i is None:
            return None
        return self.values[i]

    def get_num_items(self):
        """Returns the number of entries in the table."""
        return self.num_items

    def get_table_size(self):
        """Returns the size of the hash table."""
        return self.table_size

    def get_load_factor(self):
        """Returns the load factor of the hash table (entries / table_size)."""
        return self.get_num_items() / self.get_table_size()

