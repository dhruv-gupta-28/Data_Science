"""
Program 20: Difference between Recursion and Iteration

This program demonstrates the differences between recursive and iterative
approaches for the same problems, showing advantages and disadvantages of each.
"""

# ========== FACTORIAL ==========
def factorial_recursive(n):
    """Factorial using recursion."""
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


def factorial_iterative(n):
    """Factorial using iteration."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# ========== FIBONACCI ==========
def fibonacci_recursive(n):
    """Fibonacci using recursion (inefficient for large n)."""
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n):
    """Fibonacci using iteration (efficient)."""
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# ========== SUM OF DIGITS ==========
def sum_digits_recursive(n):
    """Sum of digits using recursion."""
    if n < 10:
        return n
    return (n % 10) + sum_digits_recursive(n // 10)


def sum_digits_iterative(n):
    """Sum of digits using iteration."""
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


# ========== REVERSE STRING ==========
def reverse_string_recursive(s):
    """Reverse string using recursion."""
    if len(s) <= 1:
        return s
    return reverse_string_recursive(s[1:]) + s[0]


def reverse_string_iterative(s):
    """Reverse string using iteration."""
    result = ""
    for char in s:
        result = char + result
    return result


# ========== BINARY SEARCH ==========
def binary_search_recursive(arr, target, start=0, end=None):
    """Binary search using recursion."""
    if end is None:
        end = len(arr) - 1
    if start > end:
        return -1
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    if arr[mid] > target:
        return binary_search_recursive(arr, target, start, mid - 1)
    return binary_search_recursive(arr, target, mid + 1, end)


def binary_search_iterative(arr, target):
    """Binary search using iteration."""
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1


def compare_approaches():
    """
    Compare recursive and iterative approaches with examples.
    """
    print("=" * 70)
    print("RECURSION vs ITERATION - Comparison")
    print("=" * 70)
    
    print("""
KEY DIFFERENCES:
----------------

1. DEFINITION:
   - Recursion: Function calls itself to solve a problem
   - Iteration: Uses loops (for/while) to repeat operations

2. MEMORY USAGE:
   - Recursion: Uses call stack (more memory overhead)
   - Iteration: Uses fixed memory (more efficient)

3. CODE READABILITY:
   - Recursion: Often more elegant and closer to mathematical definition
   - Iteration: More explicit, easier to understand for some

4. PERFORMANCE:
   - Recursion: Can be slower due to function call overhead
   - Iteration: Generally faster, no function call overhead

5. STACK OVERFLOW:
   - Recursion: Risk of stack overflow for deep recursion
   - Iteration: No stack overflow risk

6. WHEN TO USE:
   - Recursion: Tree/graph problems, divide-and-conquer, naturally recursive problems
   - Iteration: Simple loops, when performance is critical, avoiding stack overflow

""")
    
    print("-" * 70)
    print("EXAMPLE COMPARISONS:")
    print("-" * 70)
    
    # Factorial
    print("\n1. FACTORIAL:")
    print("-" * 70)
    n = 5
    rec_result = factorial_recursive(n)
    iter_result = factorial_iterative(n)
    print(f"Input: {n}")
    print(f"Recursive: factorial_recursive({n}) = {rec_result}")
    print(f"Iterative: factorial_iterative({n}) = {iter_result}")
    print(f"Match: {rec_result == iter_result}")
    
    # Fibonacci
    print("\n2. FIBONACCI:")
    print("-" * 70)
    n = 8
    rec_result = fibonacci_recursive(n)
    iter_result = fibonacci_iterative(n)
    print(f"Input: {n}")
    print(f"Recursive: fibonacci_recursive({n}) = {rec_result}")
    print(f"Iterative: fibonacci_iterative({n}) = {iter_result}")
    print(f"Match: {rec_result == iter_result}")
    print("Note: Recursive version is inefficient for large n (exponential time)")
    
    # Sum of digits
    print("\n3. SUM OF DIGITS:")
    print("-" * 70)
    n = 12345
    rec_result = sum_digits_recursive(n)
    iter_result = sum_digits_iterative(n)
    print(f"Input: {n}")
    print(f"Recursive: sum_digits_recursive({n}) = {rec_result}")
    print(f"Iterative: sum_digits_iterative({n}) = {iter_result}")
    print(f"Match: {rec_result == iter_result}")
    
    # Reverse string
    print("\n4. REVERSE STRING:")
    print("-" * 70)
    s = "hello"
    rec_result = reverse_string_recursive(s)
    iter_result = reverse_string_iterative(s)
    print(f"Input: '{s}'")
    print(f"Recursive: reverse_string_recursive('{s}') = '{rec_result}'")
    print(f"Iterative: reverse_string_iterative('{s}') = '{iter_result}'")
    print(f"Match: {rec_result == iter_result}")
    
    # Binary search
    print("\n5. BINARY SEARCH:")
    print("-" * 70)
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 7
    rec_result = binary_search_recursive(arr, target)
    iter_result = binary_search_iterative(arr, target)
    print(f"Array: {arr}")
    print(f"Target: {target}")
    print(f"Recursive: binary_search_recursive(arr, {target}) = {rec_result}")
    print(f"Iterative: binary_search_iterative(arr, {target}) = {iter_result}")
    print(f"Match: {rec_result == iter_result}")
    
    print("\n" + "=" * 70)
    print("SUMMARY TABLE:")
    print("=" * 70)
    print("""
Aspect              | Recursion              | Iteration
--------------------|------------------------|------------------------
Memory              | Call stack overhead    | Fixed memory
Performance         | Slower (function calls) | Faster
Readability         | Elegant, mathematical  | Explicit, clear
Stack Overflow      | Possible               | Not possible
Best For            | Tree/graph problems    | Simple loops
                    | Divide & conquer       | Performance-critical
                    | Naturally recursive    | Avoiding deep calls
Code Size           | Often shorter          | Often longer
Debugging           | Can be harder          | Easier to debug
""")
    
    print("\n" + "=" * 70)
    print("CONCLUSION:")
    print("=" * 70)
    print("""
- Use RECURSION when:
  * Problem is naturally recursive (trees, graphs)
  * Code clarity is more important than performance
  * Problem size is guaranteed to be small
  * Mathematical elegance is desired

- Use ITERATION when:
  * Performance is critical
  * Problem size can be very large
  * Memory efficiency is important
  * Avoiding stack overflow is necessary
  * Simple loop-based solution exists

- Many problems can be solved both ways
- Choose based on context, requirements, and constraints
""")


# Test cases
if __name__ == "__main__":
    compare_approaches()
    
    print("\n" + "=" * 70)
    print("QUICK TEST:")
    print("=" * 70)
    
    # Test all functions
    print("\nTesting all implementations:")
    print("-" * 70)
    
    test_cases = {
        "factorial": (5, factorial_recursive, factorial_iterative),
        "fibonacci": (8, fibonacci_recursive, fibonacci_iterative),
        "sum_digits": (12345, sum_digits_recursive, sum_digits_iterative),
        "reverse_string": ("python", reverse_string_recursive, reverse_string_iterative),
    }
    
    for name, (input_val, rec_func, iter_func) in test_cases.items():
        rec_result = rec_func(input_val)
        iter_result = iter_func(input_val)
        match = "✓" if rec_result == iter_result else "✗"
        print(f"{name:20} | Recursive: {str(rec_result):15} | Iterative: {str(iter_result):15} | {match}")
