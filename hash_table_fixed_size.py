class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash(self, key):
        return key % self.size

    def insert(self, key):
        i = self.hash(key)
        start = i
        while self.table[i] is not None and self.table[i] != -1:
            i = (i + 1) % self.size
            if i == start: return print("Table Full!")
        self.table[i] = key

    def search(self, key):
        i = self.hash(key)
        start = i
        while self.table[i] is not None:
            if self.table[i] == key: return i
            i = (i + 1) % self.size
            if i == start: break
        return -1

    def delete(self, key):
        pos = self.search(key)
        if pos != -1: self.table[pos] = -1
        else: print("Key not found!")

    def display(self):
        for i, v in enumerate(self.table):
            print(i, ":", v)

# Example usage
h = HashTable(7)
h.insert(10)
h.insert(20)
h.insert(5)
h.insert(15)
h.display()
print("Search 20:", h.search(20))
h.delete(20)
print("After deleting 20:")
h.display()