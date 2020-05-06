hash_table_size = 8

hash_table = [None] * hash_table_size


def myHash(s):
    str_bytes = s.encode()

    total = 0

    for b in str_bytes:
        total += b

        # total &= 0xffffffff               DJB2 hash
        # total &= 0xffffffffffffffff       FNV-1 hash

    return total

def hash_index(s):
    h = myHash(s)

    return h % hash_table_size

def put(key, value):
    index = hash_index(key)
    hash_table[index] = value

def get(key):
    index = hash_index(key)
    return hash_table[index]

def delete(key):
    index = hash_index(key)
    hash_table[index] = None

if __name__ == "__main__":
    print(hash_index("hello"))
    print(hash_index("foobar"))
    print(hash_index("cats"))
    print(hash_index("beej"))
    
    print(hash_table)
    put("hello", 37)
    put("foobar", 128)
    put("cats", "dogs")

    print(hash_table)

    print(get("hello"))
    print(get("beej"))
    print(get("foobaz"))

    delete("hello")
    print(get("hello"))

    print(hash_table)