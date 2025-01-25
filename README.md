# Assignment-3
Understanding Algorithm Efficiency and Scalability
# Hash Table with Chaining

This repository contains a Python hash table implementation using chaining to resolve collisions. It supports:
- **Insert**: Add a key-value pair.
- **Search**: Retrieve a value for a key.
- **Delete**: Remove a key-value pair.

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Ankurjhaai0408/Assignment-3.git
   ```
2. Navigate to the folder:
   ```bash
   cd Assignment-3
   ```
3. Run the script:
   ```bash
   python hash_table.py
   ```

---

## Example Usage

```python
from hash_table import HashTable

# Create a hash table
ht = HashTable(size=10)

# Insert data
ht.insert("Alice", 25)
ht.insert("Bob", 30)

# Search data
print(ht.search("Alice"))  # Output: 25

# Delete data
ht.delete("Bob")
print(ht.search("Bob"))  # Output: None

# Display table
ht.display()
```

---

## Key Insights

- **Average-Case**: Insert, search, and delete run in \(O(1)\) assuming a uniform key distribution.
- **Worst-Case**: Performance degrades to \(O(n)\) when many keys hash to the same bucket.
- The universal hash function used minimizes collisions in practice.

---

## Notes
Consider resizing the table dynamically to maintain efficiency as the dataset grows.
