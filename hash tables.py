"""
Basic hash func
"""
def my_hashing_func(str, table_size):
    bytes_representation = str.encode()

    sum = 0
    for byte in bytes_representation:
        sum += byte

    return sum % table_size

class HashTable: #basic hash template code

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.count = 0

    def get_sum_slots(self):
        return len(self.storage)

    def djb2(self, key):
        """
        DJB2 hash, 32-bit
        """

        str_key = str(key).encode()

        hash_value = 5381

        for b in str_key:
            hash_value = ((hash_value << 5) + hash_value) + b
            hash_value &= 0xffffffff

        return hash_value

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the strorage capacity of the hash table
        """

        return self.djb2(key) % self.capacity
    
    def put(self, key, value):
        """"
        Store the value with the given key
        """
        index = self.hash_index(key)
        self.storage[index] = value
        return 


    def delete(self, key):
        """
        Remove the value stored eith the given key.
        print a warning if the key is not found
        """
        index = self.hash_index(key)
        self.storage[index] = None

    def get(self, key):
        """
        Retrieve the value store with the given key
        Returns None if the key is not found
        """
        index = self.hash_index(key)
        return self.storage[index]


"""
Linked List Chaining

"""
class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

class HashTable:
    """
    A hash table with `capacity` buckets
    that accepts string keys
    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.item_count = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)
        One of the tests relies on this.
        Implement this.
        """
        # Your code here

    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        Implement this.
        """
        return len(self.storage)

    def djb2(self, key):
        """
        DJB2 hash, 32-bit
        Implement this, and/or FNV-1.
        """
        str_key = str(key).encode()

        hash = FNV_offset_basis_64

        for b in str_key:
            hash *= FNV_prime_64
            hash ^= b
            hash &= 0xffffffffffffffff  # 64-bit hash

        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index between within the hash table's storage capacity.
        """
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        index = self.hash_index(key)

        current_entry = self.storage[index]

        while current_entry is not None and current_entry != key:
           current_entry = current_entry.next

        if current_entry is not None:
            current_entry.value = value
        else:
            new_entry = HashTableEntry(key, value)
            new_entry.next = self = self,storage[index]
            self.storage[index] = new_entry

    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        # Your code here

    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        # Your code here



     
