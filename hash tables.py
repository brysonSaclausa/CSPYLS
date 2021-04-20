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
        """"
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

    def get(self, key);
        """
        Retrieve the value store with the given key
        Returns None if the key is not found
        """
        index = self.hash_index(key)
        return self.storage[index]






     
