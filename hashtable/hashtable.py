class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * self.capacity


    def djb2(self, key):
        hash = 5381
        for x in key:
            hash = (( hash << 5 ) + hash ) + ord(x)
        return hash & 0xFFFFFFFF


    def hash_index(self, key):
        return self.djb2(key) % self.capacity


    def put(self, key, value):
        index = self.hash_index(key)  # find the hash index
        node = self.storage[index]
        if node is None:                                            # nothing there, write
            self.storage[index] = HashTableEntry(key, value)
        else:
            if node.key != key:  
                while node.next is not None:                        # full, keep going
                    if node.key != key:  
                        node = node.next  
                    else:
                        node.value = value                          # nothing there, write
                if node.key == key:  
                    node.value = value                              # found match, overwrite
                else:
                    node.next = HashTableEntry(key, value)          # move to None, attach to the end
            else:
                node.value = value


    def get(self, key):
        index = self.hash_index(key)
        node = self.storage[index]
        if node is not None:                                        # continue to look
            while node.next is not None:                            
                if node.key == key:                                 # found and return
                    return node.value  
                else:
                    node = node.next                                # check again
            if node.key == key:                                     
                return node.value                                   # found it, next value is None
            return None                                             # (should never get here)
        return None                                                 # It's not there


    def delete(self, key):
        if self.get(key) is not None:                               # call 'get' to make sure we have the it
            index = self.hash_index(key)
            node = self.storage[index]
            while node.next is not None:                            # not at the end of the list
                if node.key == key:                                 # found it
                    node.key = node.next.key                        # skipping over key - assigning next
                    node.value = node.next.value                    # skipping over value - assigning next
                    return
                else:
                    node = node.next                                # keep looking
            if node.key == key:                                     # cheking the last item
                node.key = None
                node.value = None                                   # ^V setting everythin to None
                node.next = None
            return None                                             # (should never get here)
        return None                                                 # there was nothing to delete


    def resize(self, capacity=None):
        if capacity is not None:                                    # changing to assigned capacity
            self.capacity = capacity
        else:
            self.capacity = self.capacity * 2                       # reseting to starting capacity
        oldStorage = self.storage                                     # assigning current storage before reset
        self.storage = [None] * self.capacity                       # reseting storage to start
        for x in oldStorage:
            while x is not None:
                prev = x                                            # set prev to x
                x = prev.next                                       # set x to next value
                prev.next = None                                    # set the end to None
                self.put(prev.key, prev.value)                      # call PUT on current pair in oldStorage



if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # # Test resizing
    # old_capacity = len(ht.storage)
    # ht.resize()
    # new_capacity = len(ht.storage)

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # print(ht.get("line_1"))
    # print(ht.get("line_2"))
    # print(ht.get("line_3"))

    # print("")
