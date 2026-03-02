"""
Searching and Sorting: Advanced Algorithms
===========================================

Topics Covered:
- Advanced search variations
- Heap sort algorithm
- Counting sort
- Radix sort
- Bucket sort
- Algorithm optimization
"""

import heapq
import math

# ============================================================================
# 1. JUMP SEARCH
# ============================================================================

print("--- Jump Search ---")

def jump_search(arr, target):
    """Jump search - more efficient than linear, less complex than binary"""
    n = len(arr)
    step = math.sqrt(n)
    prev = 0
    
    # Find block where element is present
    while arr[min(step, n) - 1] < target:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return -1
    
    # Linear search in block
    while arr[int(prev)] < target:
        prev += 1
        if prev == min(step, n):
            return -1
    
    if arr[int(prev)] == target:
        return int(prev)
    
    return -1

arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
result = jump_search(arr, 55)
print(f"Jump search for 55: found at index {result}")
print(f"Time complexity: O(√n)")

# ============================================================================
# 2. INTERPOLATION SEARCH
# ============================================================================

print("\n--- Interpolation Search ---")

def interpolation_search(arr, target):
    """Interpolation search - better for uniformly distributed data"""
    left = 0
    right = len(arr) - 1
    
    while left <= right and target >= arr[left] and target <= arr[right]:
        # Estimate position
        pos = left + int((target - arr[left]) / (arr[right] - arr[left]) * (right - left))
        
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            left = pos + 1
        else:
            right = pos - 1
    
    return -1

arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
result = interpolation_search(arr, 60)
print(f"Interpolation search for 60: found at index {result}")
print(f"Time complexity: O(log log n) average")

# ============================================================================
# 3. HEAP SORT
# ============================================================================

print("\n--- Heap Sort ---")

def heap_sort(arr):
    """Sort using heap (heapify)"""
    n = len(arr)
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements from heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    
    return arr

def heapify(arr, n, i):
    """Maintain heap property"""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

unsorted = [64, 34, 25, 12, 22, 11, 90]
sorted_heap = heap_sort(unsorted.copy())
print(f"Heap sorted: {sorted_heap}")
print(f"Time complexity: O(n log n)")
print(f"Space complexity: O(1)")

# ============================================================================
# 4. COUNTING SORT
# ============================================================================

print("\n--- Counting Sort ---")

def counting_sort(arr, max_val=None):
    """Sort using count of each number"""
    if not arr:
        return arr
    
    if max_val is None:
        max_val = max(arr)
    
    # Count occurrences
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    
    # Reconstruct array
    result = []
    for i in range(len(count)):
        result.extend([i] * count[i])
    
    return result

unsorted = [4, 2, 2, 8, 3, 3, 1]
sorted_count = counting_sort(unsorted, max(unsorted))
print(f"Counting sorted: {sorted_count}")
print(f"Time complexity: O(n + k), where k = max value")
print(f"Space complexity: O(k)")

# ============================================================================
# 5. RADIX SORT
# ============================================================================

print("\n--- Radix Sort ---")

def radix_sort(arr):
    """Sort using radix (digit by digit)"""
    if not arr:
        return arr
    
    max_val = max(arr)
    exp = 1  # Current digit
    
    while max_val // exp > 0:
        arr = counting_sort_digit(arr, exp)
        exp *= 10
    
    return arr

def counting_sort_digit(arr, exp):
    """Counting sort for specific digit"""
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    # Store counts
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    
    # Change count to positions
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Build output
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        count[index] -= 1
        output[count[index]] = arr[i]
    
    return output

unsorted = [170, 45, 75, 90, 2, 802, 24, 2, 66]
sorted_radix = radix_sort(unsorted.copy())
print(f"Radix sorted: {sorted_radix}")
print(f"Time complexity: O(d × (n + k)), where d = digits, k = base")

# ============================================================================
# 6. BUCKET SORT
# ============================================================================

print("\n--- Bucket Sort ---")

def bucket_sort(arr):
    """Sort using buckets"""
    if len(arr) == 0:
        return arr
    
    # Create buckets
    min_val = min(arr)
    max_val = max(arr)
    bucket_count = len(arr)
    bucket_range = (max_val - min_val) / bucket_count
    
    buckets = [[] for _ in range(bucket_count)]
    
    # Put elements in buckets
    for num in arr:
        if num == max_val:
            idx = bucket_count - 1
        else:
            idx = int((num - min_val) / bucket_range)
        buckets[idx].append(num)
    
    # Sort individual buckets and concatenate
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))
    
    return sorted_arr

unsorted = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
sorted_bucket = bucket_sort(unsorted)
print(f"Bucket sorted: {sorted_bucket}")
print(f"Time complexity: O(n² ) worst, O(n + k) average")

# ============================================================================
# 7. STABILITY OF SORTS
# ============================================================================

print("\n--- Stable vs Unstable Sorts ---")

# Stable sort preserves relative order of equal elements
data = [(1, 'a'), (2, 'b'), (1, 'c'), (2, 'd')]
print("Original:", data)

# Using sorted (stable)
stable = sorted(data, key=lambda x: x[0])
print("Stable sort (by first element):", stable)

# Note: selection sort is unstable, but we can make it stable
# by using different techniques

# ============================================================================
# 8. EXTERNAL SORTING (SIMULATED)
# ============================================================================

print("\n--- External Sorting (Merge External Lists) ---")

def merge_sorted_lists(*lists):
    """Merge multiple sorted lists"""
    import heapq
    return list(heapq.merge(*lists))

list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
list3 = [1, 2, 9, 10]

merged = merge_sorted_lists(list1, list2, list3)
print(f"Merged sorted lists: {merged}")

# ============================================================================
# 9. ALGORITHM COMPARISON AND ANALYSIS
# ============================================================================

print("\n--- Algorithm Time Complexity Comparison ---")

comparison = """
Algorithm        | Best Case   | Average     | Worst Case  | Space | Stable
Bubble Sort      | O(n)        | O(n²)       | O(n²)       | O(1)  | Yes
Selection Sort   | O(n²)       | O(n²)       | O(n²)       | O(1)  | No
Insertion Sort   | O(n)        | O(n²)       | O(n²)       | O(1)  | Yes
Merge Sort       | O(n log n)  | O(n log n)  | O(n log n)  | O(n)  | Yes
Quick Sort       | O(n log n)  | O(n log n)  | O(n²)       | O(log n) | No
Heap Sort        | O(n log n)  | O(n log n)  | O(n log n)  | O(1)  | No
Counting Sort    | O(n + k)    | O(n + k)    | O(n + k)    | O(k)  | Yes
Radix Sort       | O(d×(n+k))  | O(d×(n+k))  | O(d×(n+k))  | O(n)  | Yes
Bucket Sort      | O(n + k)    | O(n + k)    | O(n²)       | O(n)  | Yes
Jump Search      | O(1)        | O(√n)       | O(√n)       | O(1)  | N/A
Interpolation    | O(1)        | O(log log n)| O(n)        | O(1)  | N/A
Binary Search    | O(1)        | O(log n)    | O(log n)    | O(1)  | N/A
"""

print(comparison)

# ============================================================================
# 10. PRACTICE PROBLEMS
# ============================================================================

print("\n--- Practice Problems ---")

# Problem 1: K largest elements
print("\nProblem 1: K Largest Elements")
def k_largest(arr, k):
    """Find k largest elements using heap"""
    return heapq.nlargest(k, arr)

result = k_largest([1, 7, 3, 2, 5, 9, 4, 8, 6], 3)
print(f"3 largest elements: {result}")

# Problem 2: Sort array of strings by length then alphabetically
print("\nProblem 2: Multi-Key Sort")
words = ['apple', 'pie', 'banana', 'cat', 'dog', 'elephant']
sorted_words = sorted(words, key=lambda x: (len(x), x))
print(f"Sorted by length then alphabetically: {sorted_words}")

# ============================================================================
# 11. CHALLENGES
# ============================================================================

print("\n--- Challenges ---")

# Challenge 1: Shell sort
print("\nChallenge 1: Shell Sort Implementation")
# TODO: Implement Shell sort (generalization of insertion sort)

# Challenge 2: Cocktail sort
print("\nChallenge 2: Cocktail Sort (Bidirectional Bubble)")
# TODO: Implement cocktail sort (bidirectional bubble sort)

# Challenge 3: Introspective sort
print("\nChallenge 3: Introspective Sort")
# TODO: Implement introspective sort (hybrid of quick, heap, insertion)
