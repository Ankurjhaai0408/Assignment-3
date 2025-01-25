import random

class HashTable:
    def __init__(self, size=101):
        """Initialize the hash table with a specified size."""
        self.size = size  # Number of slots in the hash table
        self.table = [[] for _ in range(size)]  # Each slot is a list (for chaining)

        # Universal hash function parameters
        self.p = 2 ** 31 - 1  # A large prime number
        self.a = random.randint(1, self.p - 1)
        self.b = random.randint(0, self.p - 1)

    def _hash_function(self, key):
        """Universal hash function to map a key to a bucket index."""
        hash_code = hash(key)  # Python's built-in hash
        return ((self.a * hash_code + self.b) % self.p) % self.size

    def insert(self, key, value):
        """Insert a key-value pair into the hash table."""
        index = self._hash_function(key)
        # Check if the key already exists and update it
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        # Otherwise, insert the new key-value pair
        self.table[index].append([key, value])

    def search(self, key):
        """Search for a value associated with a given key."""
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]  # Return the value
        return None  # Key not found

    def delete(self, key):
        """Delete a key-value pair from the hash table."""
        index = self._hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                self.table[index].pop(i)  # Remove the key-value pair
                return True
        return False  # Key not found

    def display(self):
        """Display the hash table for debugging purposes."""
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")

# Create a hash table
hash_table = HashTable(size=10)

# Insert key-value pairs
hash_table.insert("Alice", 25)
hash_table.insert("Bob", 30)
hash_table.insert("Charlie", 35)

# Search for keys
print(hash_table.search("Alice"))  # Output: 25
print(hash_table.search("Bob"))    # Output: 30
print(hash_table.search("Eve"))    # Output: None

# Delete a key
hash_table.delete("Bob")
print(hash_table.search("Bob"))    # Output: None

# Display the hash table
hash_table.display()
