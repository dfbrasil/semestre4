class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return (2 * key + 5) % self.size

    def insert_key(self, key):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = [key]
        else:
            self.table[index].append(key)

    def display_table(self):
        for i, chain in enumerate(self.table):
            print(f"Index {i}: {chain}")

def main():
    keys = [12, 44, 13, 88, 23, 94, 11, 39, 20, 16, 5]
    hash_table = HashTable(size=11)

    for key in keys:
        hash_table.insert_key(key)

    hash_table.display_table()

if __name__ == "__main__":
    main()

