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
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity

        # initial size of hash table
        self.storage = [None] * (self.capacity)

        # amount of stored info in hash table
        self.count = 0
        

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here

        # indicates the number of slots available in hash table
        return len(self.storage)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here

        # load factor formula is number of items in hash table / total number of slots
        load_factor = self.count/self.capacity
        

        if not self.resize:
            # check load factor, if bigger than given value, double capacity
            if load_factor > 0.7:
                self.resize(int(self.capacity * 2))
            # check load factor, if bigger than given value, half the capacity
            elif load_factor < 0.2 and self.capacity != MIN_CAPACITY:
                self.resize(int(self.capacity / 2))

        return load_factor



    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here

        # hashing function found online
        hashed = 5381
        for c in key:
            hashed = (hashed * 33) + ord(c)
        return hashed


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity

        # determines index by hash function modulo capacity, the remainder is the index
        # on which the data will be stored
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        

        # with collisions/without linked list:
        # idx = self.hash_index(key)
        # self.storage[idx] = value


        slot = self.hash_index(key)
        cur = self.storage[slot]

        # if cur exists
        if cur:
            # loop through the list by checking cur.next each time
            # and also see if cur.key is the same key that is being searched
            while cur.next != None and cur.key != key:
                cur = cur.next
            # if there is already the key, overwrite the value
            if cur.key == key:
                cur.value = value
            # if key doesn't exist 
            # make a new entry with cur.next
            # increase count by 1
            else:
                cur.next = HashTableEntry(key, value)
                self.count += 1

        # else, make new entry
        # increase count
        else:
            self.storage[slot] = HashTableEntry(key, value)
            self.count += 1
   

  



    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        # pass key to hash method 
        # idx = self.hash_index(key)
        # # and set it as None(default value)
        # self.storage[idx] = None

        index = self.hash_index(key)
        cur = self.storage[index]

        # if value at index is empty then return
        if cur is None:
            return

        # else
        while cur:
            # if there is a same key, update with its next value
           
            if cur.key == key:
                # change pointer to another index
                self.storage[index] = cur.next
                 # reduce the slot count
                self.count -= 1
            cur = cur.next

        return None




    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        # idx = self.hash_index(key)
        # return self.storage[idx]

        slot = self.hash_index(key)
        cur = self.storage[slot]
        # if cur exists
        while cur:
            # check for the current key
            # if the current key exists, return the value of it
            if cur.key == key:
                return cur.value

            # else, keep searching by checking the next, and so on
            cur = cur.next

        # If the value that is being looked for is not there, return None
        return None





    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here

        # create new instance of HashTable
        # new capacity determined by get_load_factor
        new_table = HashTable(new_capacity)

        
        for n in self.storage:
            # checks if it exists and it is the last
            if n != None and n.next == None:
                #  create new table and distribute data to match new size
                new_table.put(n.key, n.value)
            else:
                curr_node = n
                while curr_node != None:
                    # while there are available slots, rehash the key/value pairs
                    new_table.put(curr_node.key, curr_node.value)
                    # once those are filled, set current node to the next to fill
                    curr_node = curr_node.next


        # Set the properties of the class to the new Instance table with the
        # new properties      
        self.capacity = new_table.capacity
        self.storage = new_table.storage
        self.count = new_table.count

   



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
