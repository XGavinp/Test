import hashlib
from bitarray import bitarray

class BloomFilter:
    def __init__(self, size, hash_count):
        """
        Initialize the Bloom Filter.

        :param size: Size of the bit array.
        :param hash_count: Number of hash functions.
        """
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def _hashes(self, item):
        """
        Generate hash values for the given item.

        :param item: Item to hash.
        :return: List of hash values.
        """
        hashes = []
        item = item.encode('utf-8')
        for i in range(self.hash_count):
            # Use different salts to simulate different hash functions
            hash_result = hashlib.sha256(item + i.to_bytes(2, byteorder='little')).hexdigest()
            hash_int = int(hash_result, 16)
            hashes.append(hash_int % self.size)
        return hashes

    def add(self, item):
        """
        Add an item to the Bloom Filter.

        :param item: Item to add.
        """
        for hash_val in self._hashes(item):
            self.bit_array[hash_val] = 1

    def __contains__(self, item):
        """
        Check if an item is possibly in the Bloom Filter.

        :param item: Item to check.
        :return: True if possibly present, False if definitely not.
        """
        return all(self.bit_array[hash_val] for hash_val in self._hashes(item))
