"""
Searching and Sorting: Practice Problems and Solutions
=======================================================

Topics Covered:
- Practical algorithm problems
- Algorithm selection and optimization
- Problem-solving strategies
- Real-world applications
"""

import time
from collections import Counter

# ============================================================================
# 1. SEARCH IN ROTATED SORTED ARRAY
# ============================================================================

print("--- Problem 1: Search in Rotated Sorted Array ---")

def search_rotated(arr, target):
    """Find target in rotated sorted array"""
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        
        # Determine which side is sorted
        if arr[left] <= arr[mid]:  # Left side sorted
            if arr[left] <= target < arr[mid]:
                right = mid - 1  # Search left
            else:
                left = mid + 1   # Search right
        else:  # Right side sorted
            if arr[mid] < target <= arr[right]:
                left = mid + 1   # Search right
            else:
                right = mid - 1  # Search left
    
    return -1

arr = [4, 5, 6, 7, 0, 1, 2]
target = 0
result = search_rotated(arr, target)
print(f"Search in rotated array: {result}")
print(f"Time complexity: O(log n)")

# ============================================================================
# 2. TWO SUM PROBLEM
# ============================================================================

print("\n--- Problem 2: Two Sum (Find Pair with Target Sum) ---")

def two_sum_sorted(arr, target):
    """Find two numbers that sum to target in sorted array"""
    left = 0
    right = len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return (arr[left], arr[right])
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return None

arr = [2, 7, 11, 15, 20]
target = 22
result = two_sum_sorted(arr, target)
print(f"Two sum: {result}")
print(f"Time complexity: O(n)")

# ============================================================================
# 3. KTH SMALLEST ELEMENT
# ============================================================================

print("\n--- Problem 3: Kth Smallest Element ---")

def find_kth_smallest(arr, k):
    """Find kth smallest element"""
    # Using sorting
    return sorted(arr)[k - 1]

def find_kth_smallest_heap(arr, k):
    """Find kth smallest using max heap"""
    import heapq
    return heapq.nsmallest(k, arr)[-1]

arr = [3, 2, 1, 5, 6, 4]
k = 2
result1 = find_kth_smallest(arr, k)
result2 = find_kth_smallest_heap(arr, k)
print(f"Kth smallest: {result1}")
print(f"Time complexity - sort: O(n log n), heap: O(n log k)")

# ============================================================================
# 4. MERGE SORTED ARRAYS
# ============================================================================

print("\n--- Problem 4: Merge Sorted Arrays ---")

def merge_sorted_arrays(arr1, arr2):
    """Merge two sorted arrays"""
    result = []
    i = j = 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    
    return result

arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
merged = merge_sorted_arrays(arr1, arr2)
print(f"Merged: {merged}")
print(f"Time complexity: O(n + m)")

# ============================================================================
# 5. SORT COLORS (0s, 1s, 2s)
# ============================================================================

print("\n--- Problem 5: Sort Colors ---")

def sort_colors(arr):
    """Sort array of 0s, 1s, and 2s in-place"""
    red = white = blue = 0
    
    # Count occurrences
    for num in arr:
        if num == 0:
            red += 1
        elif num == 1:
            white += 1
        else:
            blue += 1
    
    # Reconstruct
    for i in range(red):
        arr[i] = 0
    for i in range(red, red + white):
        arr[i] = 1
    for i in range(red + white, len(arr)):
        arr[i] = 2

arr = [2, 0, 2, 1, 1, 0]
sort_colors(arr)
print(f"Sorted colors: {arr}")
print(f"Time complexity: O(n)")

# ============================================================================
# 6. PEAK ELEMENT
# ============================================================================

print("\n--- Problem 6: Find Peak Element ---")

def find_peak(arr):
    """Find peak element (local maximum)"""
    left = 0
    right = len(arr) - 1
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid + 1]:
            right = mid
        else:
            left = mid + 1
    
    return left

arr = [1, 2, 3, 1]
peak_idx = find_peak(arr)
print(f"Peak element index: {peak_idx}, value: {arr[peak_idx]}")
print(f"Time complexity: O(log n)")

# ============================================================================
# 7. MISSING NUMBER
# ============================================================================

print("\n--- Problem 7: Find Missing Number ---")

def find_missing(arr):
    """Find missing number in array 0 to n"""
    n = len(arr)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

arr = [0, 1, 3]  # Missing 2
missing = find_missing(arr)
print(f"Missing number: {missing}")
print(f"Time complexity: O(n)")

# ============================================================================
# 8. MAJORITY ELEMENT
# ============================================================================

print("\n--- Problem 8: Majority Element ---")

def majority_element(arr):
    """Find element appearing more than n/2 times"""
    # Method 1: Using counter
    counter = Counter(arr)
    for num, count in counter.items():
        if count > len(arr) // 2:
            return num
    
    # Method 2: Boyer-Moore voting (more elegant)
    # candidate = None
    # count = 0
    # for num in arr:
    #     if count == 0:
    #         candidate = num
    #     count += (1 if num == candidate else -1)
    # return candidate

arr = [2, 2, 1, 1, 1, 2, 2]
result = majority_element(arr)
print(f"Majority element: {result}")
print(f"Time complexity: O(n)")

# ============================================================================
# 9. FIRST BAD VERSION (BINARY SEARCH)
# ============================================================================

print("\n--- Problem 9: First Bad Version ---")

def first_bad_version(n, bad_version):
    """Find first bad version using binary search"""
    def is_bad(version):
        return version >= bad_version
    
    left = 1
    right = n
    
    while left < right:
        mid = (left + right) // 2
        if is_bad(mid):
            right = mid
        else:
            left = mid + 1
    
    return left

first_bad = first_bad_version(5, 4)
print(f"First bad version: {first_bad}")
print(f"Time complexity: O(log n)")

# ============================================================================
# 10. SQUARE ROOT OF INTEGER
# ============================================================================

print("\n--- Problem 10: Square Root (Integer) ---")

def sqrt_integer(x):
    """Find integer square root"""
    if x < 2:
        return x
    
    left = 1
    right = x
    
    while left <= right:
        mid = (left + right) // 2
        sq = mid * mid
        
        if sq == x:
            return mid
        elif sq < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return right  # Floor square root

result = sqrt_integer(16)
print(f"Square root of 16: {result}")
print(f"Time complexity: O(log n)")

# ============================================================================
# 11. PERFORMANCE COMPARISON
# ============================================================================

print("\n--- Performance Comparison ---")

import random

# Generate random data
data = [random.randint(1, 1000) for _ in range(1000)]

# Time different sorting algorithms
def bubble_sort_time(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def python_sort_time(arr):
    return sorted(arr)

# Time bubble sort
start = time.time()
bubble_sort_time(data)
bubble_time = time.time() - start

# Time Python's sort
start = time.time()
python_sort_time(data)
python_time = time.time() - start

print(f"Bubble sort: {bubble_time*1000:.2f}ms")
print(f"Python sort (Timsort): {python_time*1000:.2f}ms")
print(f"Speedup: {bubble_time/python_time:.1f}x")

# ============================================================================
# 12. CHALLENGES
# ============================================================================

print("\n--- Challenges ---")

# Challenge 1: K closest elements to x
print("\nChallenge 1: K Closest Elements")
# TODO: Find k closest elements to x in sorted array

# Challenge 2: Longest increasing subsequence
print("\nChallenge 2: Longest Increasing Subsequence")
# TODO: Find longest increasing subsequence

# Challenge 3: Meeting rooms scheduler
print("\nChallenge 3: Meeting Rooms")
# TODO: Determine if person can attend all meetings

# Challenge 4: Sort matrix diagonally
print("\nChallenge 4: Sort Matrix")
# TODO: Sort a matrix diagonally
