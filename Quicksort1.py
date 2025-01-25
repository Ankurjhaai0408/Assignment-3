import random

def randomized_partition(arr, low, high):
    """Partition the array with a random pivot."""
    pivot_index = random.randint(low, high)  # Select a random pivot
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # Swap pivot with the last element
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:  # Ensure elements <= pivot are on the left
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Place pivot in the correct position
    return i + 1

def randomized_quicksort(arr, low, high):
    """Recursive Randomized Quicksort."""
    if low < high:
        pivot_index = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, pivot_index - 1)  # Sort left subarray
        randomized_quicksort(arr, pivot_index + 1, high)  # Sort right subarray

def quicksort(arr):
    """Helper function to call randomized_quicksort."""
    if len(arr) <= 1:
        return arr  # Edge case for empty or single-element arrays
    randomized_quicksort(arr, 0, len(arr) - 1)
    return arr

# Testing the implementation
if __name__ == "__main__":
    test_cases = [
        [],  # Empty array
        [1],  # Single element
        [3, 1, 2],  # Unsorted array
        [1, 2, 3, 4, 5],  # Already sorted array
        [5, 4, 3, 2, 1],  # Reverse sorted array
        [4, 2, 2, 8, 5, 2, 2, 4],  # Array with duplicates
    ]
    
    for test in test_cases:
        print(f"Original: {test}")
        sorted_array = quicksort(test.copy())
        print(f"Sorted: {sorted_array}\n")
