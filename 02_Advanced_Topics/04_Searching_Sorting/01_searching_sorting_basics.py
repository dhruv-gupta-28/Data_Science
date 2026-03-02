"""
Advanced Topics: Searching and Sorting
=======================================

Topics Covered:
- Linear search
- Binary search
- Bubble sort
- Selection sort
- Insertion sort
- Merge sort
- Quick sort
- Python's built-in sort
- Sorting with custom keys
"""

# ============================================================================
# 1. LINEAR SEARCH
# ============================================================================

print("--- Linear Search ---")

def linear_search(lst, target):
    """Search for target in list (returns index or -1)"""
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

# Test
numbers = [64, 34, 25, 12, 22, 11, 90]
target = 22

result = linear_search(numbers, target)
print(f"Linear search for {target} in {numbers}")
print(f"Found at index: {result}")
print(f"Time complexity: O(n)")

# ============================================================================
# 2. BINARY SEARCH
# ============================================================================

print("\n--- Binary Search ---")

def binary_search(lst, target):
    """Search for target in sorted list (returns index or -1)"""
    left = 0
    right = len(lst) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Test (must be sorted!)
sorted_numbers = [11, 12, 22, 25, 34, 64, 90]
target = 25

result = binary_search(sorted_numbers, target)
print(f"Binary search for {target} in {sorted_numbers}")
print(f"Found at index: {result}")
print(f"Time complexity: O(log n)")

# ============================================================================
# 3. BUBBLE SORT
# ============================================================================

print("\n--- Bubble Sort ---")

def bubble_sort(lst):
    """Sort using bubble sort (repeatedly swap adjacent elements)"""
    n = len(lst)
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                # Swap
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        
        if not swapped:
            break
    
    return lst

# Test
unsorted = [64, 34, 25, 12, 22, 11, 90]
print(f"Original: {unsorted}")
sorted_result = bubble_sort(unsorted.copy())
print(f"Bubble sorted: {sorted_result}")
print(f"Time complexity: O(n²)")
print(f"Space complexity: O(1)")

# ============================================================================
# 4. SELECTION SORT
# ============================================================================

print("\n--- Selection Sort ---")

def selection_sort(lst):
    """Sort using selection sort (find minimum and place at start)"""
    n = len(lst)
    
    for i in range(n):
        # Find minimum element in remaining array
        min_idx = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        
        # Swap
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    
    return lst

# Test
unsorted = [64, 34, 25, 12, 22, 11, 90]
print(f"Original: {unsorted}")
sorted_result = selection_sort(unsorted.copy())
print(f"Selection sorted: {sorted_result}")
print(f"Time complexity: O(n²)")
print(f"Space complexity: O(1)")

# ============================================================================
# 5. INSERTION SORT
# ============================================================================

print("\n--- Insertion Sort ---")

def insertion_sort(lst):
    """Sort using insertion sort (build sorted array one item at a time)"""
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        
        # Move elements greater than key one position ahead
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        
        lst[j + 1] = key
    
    return lst

# Test
unsorted = [64, 34, 25, 12, 22, 11, 90]
print(f"Original: {unsorted}")
sorted_result = insertion_sort(unsorted.copy())
print(f"Insertion sorted: {sorted_result}")
print(f"Time complexity: O(n²)")
print(f"Space complexity: O(1)")

# ============================================================================
# 6. MERGE SORT
# ============================================================================

print("\n--- Merge Sort ---")

def merge_sort(lst):
    """Sort using merge sort (divide and conquer)"""
    if len(lst) <= 1:
        return lst
    
    # Divide
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    
    # Merge
    return merge(left, right)

def merge(left, right):
    """Merge two sorted lists"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Test
unsorted = [64, 34, 25, 12, 22, 11, 90]
print(f"Original: {unsorted}")
sorted_result = merge_sort(unsorted)
print(f"Merge sorted: {sorted_result}")
print(f"Time complexity: O(n log n)")
print(f"Space complexity: O(n)")

# ============================================================================
# 7. QUICK SORT
# ============================================================================

print("\n--- Quick Sort ---")

def quick_sort(lst):
    """Sort using quick sort (divide and conquer with pivot)"""
    if len(lst) <= 1:
        return lst
    
    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# Test
unsorted = [64, 34, 25, 12, 22, 11, 90]
print(f"Original: {unsorted}")
sorted_result = quick_sort(unsorted)
print(f"Quick sorted: {sorted_result}")
print(f"Time complexity: O(n log n) average, O(n²) worst")
print(f"Space complexity: O(n)")

# ============================================================================
# 8. PYTHON'S BUILT-IN SORT
# ============================================================================

print("\n--- Python's Built-in Sort ---")

# Method 1: sorted() function
unsorted = [64, 34, 25, 12, 22, 11, 90]
sorted_list = sorted(unsorted)
print(f"Using sorted(): {sorted_list}")

# Method 2: list.sort() method
unsorted = [64, 34, 25, 12, 22, 11, 90]
unsorted.sort()
print(f"Using .sort(): {unsorted}")

# Reverse sort
unsorted = [64, 34, 25, 12, 22, 11, 90]
descending = sorted(unsorted, reverse=True)
print(f"Descending: {descending}")

# ============================================================================
# 9. SORTING WITH CUSTOM KEYS
# ============================================================================

print("\n--- Sorting with Keys ---")

# Example 1: Sort by string length
words = ['python', 'java', 'c', 'javascript', 'go']
by_length = sorted(words, key=len)
print(f"Words by length: {by_length}")

# Example 2: Sort without case sensitivity
words = ['Python', 'java', 'C', 'JavaScript']
case_insensitive = sorted(words, key=str.lower)
print(f"Case insensitive: {case_insensitive}")

# Example 3: Sort tuples by specific element
students = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
by_score = sorted(students, key=lambda x: x[1])
print(f"By score: {by_score}")

# Example 4: Sort dictionaries by value
grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
by_value = sorted(grades.items(), key=lambda x: x[1])
print(f"By grade value: {by_value}")

# Example 5: Sort with multiple keys
people = [('Alice', 30), ('Bob', 25), ('Charlie', 30)]
by_age_then_name = sorted(people, key=lambda x: (x[1], x[0]))
print(f"By age then name: {by_age_then_name}")

# ============================================================================
# 10. SORTING COMPLEX OBJECTS
# ============================================================================

print("\n--- Sorting Complex Objects ---")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"Person({self.name}, {self.age})"

people = [
    Person('Alice', 30),
    Person('Bob', 25),
    Person('Charlie', 35)
]

# Sort by age
by_age = sorted(people, key=lambda p: p.age)
print(f"Sorted by age: {by_age}")

# Sort by name
by_name = sorted(people, key=lambda p: p.name)
print(f"Sorted by name: {by_name}")

# ============================================================================
# 11. ALGORITHM COMPARISON
# ============================================================================

print("\n--- Algorithm Comparison ---")

comparison_table = """
Algorithm        | Best Case   | Average     | Worst Case  | Space
Bubble Sort      | O(n)        | O(n²)       | O(n²)       | O(1)
Selection Sort   | O(n²)       | O(n²)       | O(n²)       | O(1)
Insertion Sort   | O(n)        | O(n²)       | O(n²)       | O(1)
Merge Sort       | O(n log n)  | O(n log n)  | O(n log n)  | O(n)
Quick Sort       | O(n log n)  | O(n log n)  | O(n²)       | O(log n)
Binary Search    | -           | O(log n)    | O(log n)    | O(1)
Linear Search    | O(1)        | O(n)        | O(n)        | O(1)
"""

print(comparison_table)

# ============================================================================
# 12. PRACTICE PROBLEMS
# ============================================================================

print("\n--- Practice Problems ---")

# Problem 1: Find target in array
print("\nProblem 1: Find Target")
def find_target_position(arr, target):
    """Find position of target using binary search"""
    try:
        return binary_search(arr, target)
    except:
        return -1

result = find_target_position([11, 12, 22, 25, 34, 64, 90], 25)
print(f"Position of 25: {result}")

# Problem 2: Sort and find median
print("\nProblem 2: Find Median")
def find_median(arr):
    """Find median of array"""
    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    if n % 2 == 1:
        return sorted_arr[n // 2]
    else:
        return (sorted_arr[n // 2 - 1] + sorted_arr[n // 2]) / 2

median = find_median([3, 1, 4, 1, 5, 9, 2, 6])
print(f"Median: {median}")

# ============================================================================
# 13. CHALLENGES
# ============================================================================

print("\n--- Challenges ---")

# Challenge 1: Implement counting sort
print("\nChallenge 1: Counting Sort")
# TODO: Implement counting sort for positive integers

# Challenge 2: Implement radix sort
print("\nChallenge 2: Radix Sort")
# TODO: Implement radix sort for positive integers

# Challenge 3: Find k largest elements
print("\nChallenge 3: K Largest Elements")
# TODO: Find k largest elements efficiently

# Challenge 4: Merge sorted arrays
print("\nChallenge 4: Merge Sorted Arrays")
# TODO: Merge multiple sorted arrays into one sorted array
