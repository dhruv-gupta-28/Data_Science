"""
Recursion: Reverse Word

Reverse a word recursively by extracting characters.
"""


def reverse_word(word: str) -> str:
    """
    Reverse a word recursively.
    
    Args:
        word: The word to reverse
        
    Returns:
        The reversed word
    """
    if len(word) == 0:
        return ""
    else:
        return reverse_word(word[1:]) + word[0]


if __name__ == "__main__":
    print("Word reversal examples:")
    
    words = ["Python", "hello", "world", "recursion"]
    for word in words:
        reversed_word = reverse_word(word)
        print(f"'{word}' -> '{reversed_word}'")
