"""
Recursion: Palindrome Check

Check if a word is a palindrome recursively.
"""


def is_palindrome(text: str) -> bool:
    """
    Check if text is a palindrome recursively.
    Ignores spaces and case.
    
    Args:
        text: The text to check
        
    Returns:
        True if palindrome, False otherwise
    """
    # Clean the text
    clean = text.lower().replace(" ", "")
    
    # Base case
    if len(clean) <= 1:
        return True
    
    # Check first and last characters
    if clean[0] != clean[-1]:
        return False
    
    # Recursive case
    return is_palindrome(clean[1:-1])


if __name__ == "__main__":
    print("Palindrome check examples:")
    
    test_cases = [
        "racecar",
        "hello",
        "madam",
        "A man a plan a canal Panama",
        "12321",
        "123"
    ]
    
    for word in test_cases:
        result = is_palindrome(word)
        print(f"Is '{word}' a palindrome? {result}")
