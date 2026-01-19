"""
Program 18: Solve Tower of Hanoi (basic level)

Tower of Hanoi is a classic recursion problem.
Rules:
1. Only one disk can be moved at a time
2. Only the top disk can be moved
3. No larger disk can be placed on top of a smaller disk

Base case: If n == 1, move disk from source to destination
Recursive case:
    1. Move n-1 disks from source to auxiliary
    2. Move largest disk from source to destination
    3. Move n-1 disks from auxiliary to destination
"""

def tower_of_hanoi(n, source, destination, auxiliary):
    """
    Solve Tower of Hanoi problem using recursion.
    
    Args:
        n (int): Number of disks
        source (str): Name of source rod
        destination (str): Name of destination rod
        auxiliary (str): Name of auxiliary rod
    """
    # Base case: only one disk
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    
    # Step 1: Move n-1 disks from source to auxiliary
    tower_of_hanoi(n - 1, source, auxiliary, destination)
    
    # Step 2: Move largest disk from source to destination
    print(f"Move disk {n} from {source} to {destination}")
    
    # Step 3: Move n-1 disks from auxiliary to destination
    tower_of_hanoi(n - 1, auxiliary, destination, source)


def tower_of_hanoi_with_steps(n, source, destination, auxiliary, step_count=[0]):
    """
    Solve Tower of Hanoi with step counting.
    
    Args:
        n (int): Number of disks
        source (str): Name of source rod
        destination (str): Name of destination rod
        auxiliary (str): Name of auxiliary rod
        step_count (list): List to track step count
        
    Returns:
        int: Total number of moves
    """
    if n == 1:
        step_count[0] += 1
        print(f"Step {step_count[0]}: Move disk 1 from {source} to {destination}")
        return step_count[0]
    
    # Move n-1 disks from source to auxiliary
    tower_of_hanoi_with_steps(n - 1, source, auxiliary, destination, step_count)
    
    # Move largest disk
    step_count[0] += 1
    print(f"Step {step_count[0]}: Move disk {n} from {source} to {destination}")
    
    # Move n-1 disks from auxiliary to destination
    tower_of_hanoi_with_steps(n - 1, auxiliary, destination, source, step_count)
    
    return step_count[0]


# Test cases
if __name__ == "__main__":
    print("Tower of Hanoi - Recursive Solution")
    print("-" * 40)
    
    print("\nTower of Hanoi with 3 disks:")
    print("=" * 40)
    tower_of_hanoi(3, 'A', 'C', 'B')
    
    print("\n" + "=" * 40)
    print("\nTower of Hanoi with 2 disks:")
    print("=" * 40)
    tower_of_hanoi(2, 'A', 'C', 'B')
    
    print("\n" + "=" * 40)
    print("\nTower of Hanoi with 4 disks (with step count):")
    print("=" * 40)
    step_count = [0]
    total_steps = tower_of_hanoi_with_steps(4, 'A', 'C', 'B', step_count)
    print(f"\nTotal moves required: {total_steps}")
    print(f"Formula: 2^n - 1 = 2^4 - 1 = {2**4 - 1}")
    
    # User input example
    try:
        n = int(input("\nEnter number of disks: "))
        if n < 1:
            print("Please enter a positive number.")
        else:
            print(f"\nTower of Hanoi solution for {n} disks:")
            print("=" * 40)
            step_count = [0]
            total_steps = tower_of_hanoi_with_steps(n, 'A', 'C', 'B', step_count)
            print(f"\nTotal moves: {total_steps} (Formula: 2^{n} - 1 = {2**n - 1})")
    except ValueError:
        print("Please enter a valid integer.")
