# Recursion Programs – Interview Practice List

This directory contains 20 comprehensive recursion programs for interview practice, each with detailed explanations, test cases, and examples.

## Programs List

### Basic Recursion
1. **1_factorial.py** - Find factorial of a number using recursion
2. **2_fibonacci.py** - Generate Fibonacci series using recursion
3. **3_print_1_to_n.py** - Print numbers from 1 to N using recursion
4. **4_sum_n_natural_numbers.py** - Find the sum of first N natural numbers using recursion

### String Recursion
5. **5_reverse_string.py** - Reverse a string using recursion
6. **6_palindrome_check.py** - Check whether a string is palindrome using recursion
17. **17_length_without_len.py** - Find length of a string/list without using len()

### Number Operations
7. **7_power_of_number.py** - Find power of a number (xⁿ) using recursion (includes optimized version)
8. **8_count_digits.py** - Count digits in a number using recursion
9. **9_sum_of_digits.py** - Find sum of digits of a number using recursion
15. **15_gcd.py** - Calculate GCD of two numbers using recursion (Euclidean Algorithm)

### List Operations
11. **11_max_element_list.py** - Find the maximum element in a list using recursion
12. **12_binary_search.py** - Perform binary search using recursion
13. **13_print_list_elements.py** - Print all elements of a list using recursion
14. **14_min_element_list.py** - Find minimum element in a list using recursion

### Advanced Recursion
10. **10_even_odd_indirect_recursion.py** - Check even or odd using indirect recursion
16. **16_print_n_to_1.py** - Print numbers from N to 1 using recursion
18. **18_tower_of_hanoi.py** - Solve Tower of Hanoi (basic level)

### Concepts & Explanations
19. **19_explain_loi.py** - Explain LOI (Level of Indirection) in recursion with examples
20. **20_recursion_vs_iteration.py** - Difference between recursion and iteration with comparisons

## Key Concepts

### Recursion Basics
- **Base Case**: Condition that stops recursion
- **Recursive Case**: Function calls itself with modified parameters
- **Call Stack**: Memory structure that stores function calls

### Types of Recursion
1. **Direct Recursion**: Function calls itself directly
2. **Indirect Recursion**: Function A calls function B, which calls function A
3. **Tail Recursion**: Recursive call is the last operation
4. **Tree Recursion**: Multiple recursive calls (e.g., Fibonacci)

### Important Topics
- **LOI (Level of Indirection)**: Depth of recursive calls
- **Memoization**: Storing results to avoid redundant calculations
- **Stack Overflow**: Risk when recursion is too deep
- **Time Complexity**: Understanding Big O for recursive algorithms

## How to Use

Each program is self-contained and can be run independently:

```bash
python 1_factorial.py
python 2_fibonacci.py
# ... and so on
```

All programs include:
- Detailed docstrings explaining the algorithm
- Multiple test cases
- User input examples
- Comments explaining base cases and recursive cases

## Practice Tips

1. **Understand the Base Case**: Always identify when recursion should stop
2. **Trace the Execution**: Follow the recursive calls mentally or with print statements
3. **Start Simple**: Begin with factorial and Fibonacci before moving to complex problems
4. **Compare Approaches**: Use program 20 to see recursive vs iterative solutions
5. **Visualize Recursion**: Use program 19 to understand LOI and recursion depth

## Common Patterns

### Pattern 1: Linear Recursion
```python
def function(n):
    if base_case:
        return value
    return operation(n, function(n-1))
```

### Pattern 2: Tree Recursion
```python
def function(n):
    if base_case:
        return value
    return function(n-1) + function(n-2)
```

### Pattern 3: Divide and Conquer
```python
def function(arr, start, end):
    if base_case:
        return value
    mid = (start + end) // 2
    return combine(function(arr, start, mid), 
                   function(arr, mid+1, end))
```

## Interview Preparation

These programs cover common recursion topics asked in interviews:
- ✅ Basic recursion patterns
- ✅ String manipulation
- ✅ Number operations
- ✅ List/array operations
- ✅ Advanced algorithms (Tower of Hanoi, Binary Search)
- ✅ Understanding recursion concepts (LOI, recursion vs iteration)

## Notes

- All programs handle edge cases (empty strings, negative numbers, etc.)
- Some programs include both index-based and slicing approaches
- Optimized versions are provided where applicable (e.g., power calculation)
- Each program is well-documented for learning purposes

Happy coding! 🚀
