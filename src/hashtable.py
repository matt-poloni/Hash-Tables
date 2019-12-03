# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.count = 0
        self.cap_init = capacity
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        hash_value = 5381
        for char in key:
            hash_value = ((hash_value << 5) + hash_value) ^ ord(char)
        return hash_value


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash_djb2(key) % self.capacity


    def insert(self, key, value, add=True):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        self.count += int(add)
        self.resize()
        index = self._hash_mod(key)
        new_pair = LinkedPair(key, value)
        if (pair := self.storage[index]) is not None:
            while pair is not None:
                if pair.key == key:
                    pair.value = value
                    return
                elif pair.next is not None:
                    pair = pair.next
                else:
                    pair.next = new_pair
                    return
        else:
            self.storage[index] = new_pair

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        prev = None
        if (pair := self.storage[index]) is not None:
            while pair.key != key:
                if pair.next is not None:
                    prev = pair
                    pair = pair.next
                else:
                    print(f"ERROR: '{key}' key not found")
                    return
            if prev is not None:
                prev.next = pair.next
            else:
                self.storage[index] = None
            self.count -= 1
            self.resize()
        else:
            print(f"ERROR: '{key}' key not found")


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        pair = self.storage[index]
        while pair is not None:
            if pair.key == key:
                return pair.value
            else:
                pair = pair.next
        return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        load = self.count / self.capacity
        if (overload := load > 0.7) or load < 0.2:
            old_capacity = self.capacity
            old_storage = [*self.storage]
            if overload:
                self.capacity *= 2
            elif self.cap_init < (new_cap := self.capacity // 2):
                self.capacity = new_cap
            else:
                return
            self.storage = [None] * self.capacity
            for i in range(old_capacity):
                if (pair := old_storage[i]) is not None:
                  while pair is not None:
                      self.insert(pair.key, pair.value, False)
                      pair = pair.next



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
