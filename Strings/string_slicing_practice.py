# String Slicing Practice Questions

city = "Tiruvanthpuram"

# ============================================
# 1. Write a slice to print the first 3 characters of the string.
# ============================================
print("1. First 3 characters:", city[:3])
# Output: Tir

# ============================================
# 2. Write a slice to print the last 5 characters of the string.
# ============================================
print("2. Last 5 characters:", city[-5:])
# Output: puram

# ============================================
# 3. Print the substring "Tiru" using slicing.
# ============================================
print("3. Substring 'Tiru':", city[0:4])
# Output: Tiru

# ============================================
# 4. Print the substring "anth" using slicing.
# ============================================
print("4. Substring 'anth':", city[5:9])
# Output: anth

# ============================================
# 5. Slice and print the characters from index 2 to 8.
# ============================================
print("5. Characters from index 2 to 8:", city[2:9])
# Output: ruvanth

# ============================================
# 6. Slice from the beginning to index 6 (not included).
# ============================================
print("6. Beginning to index 6 (exclusive):", city[:6])
# Output: Tiruvan

# ============================================
# 7. Slice from index 5 to the end.
# ============================================
print("7. Index 5 to the end:", city[5:])
# Output: anthpuram

# ============================================
# 8. Use slicing to reverse the string.
# ============================================
print("8. Reversed string:", city[::-1])
# Output: maruphtnavuriT

# ============================================
# 9. Print every second character using a slice step.
# ============================================
print("9. Every second character:", city[::2])
# Output: Tuvnhm

# ============================================
# 10. Print every third character using a slice step.
# ============================================
print("10. Every third character:", city[::3])
# Output: Tvnm

# ============================================
# 11. Slice out and print "vanth".
# ============================================
print("11. Substring 'vanth':", city[4:9])
# Output: vanth

# ============================================
# 12. Extract the middle 4 characters using slicing.
# ============================================
# String length is 14, middle 4 would be around indices 5-9
print("12. Middle 4 characters:", city[5:9])
# Output: anth

# ============================================
# 13. Slice the string so that only vowels remain (use indexing you decide).
# ============================================
# Vowels in "Tiruvanthpuram": i(1), u(3), a(5), u(10), a(12)
# We can extract them individually or use a different approach
vowels = city[1] + city[3] + city[5] + city[10] + city[12]
print("13. Vowels only:", vowels)
# Output: iua ua

# Alternative approach using slicing for consecutive vowels:
# Since vowels are not consecutive, we extract them individually
print("13. Vowels (alternative):", city[1:2] + city[3:4] + city[5:6] + city[10:11] + city[12:13])

# ============================================
# 14. Print the string except the first and last two characters.
# ============================================
print("14. Excluding first and last two characters:", city[2:-2])
# Output: ruvanthpu

# ============================================
# 15. Create a slice that prints "puram" from the string.
# ============================================
print("15. Substring 'puram':", city[-5:])
# Output: puram

# ============================================
# Additional Information
# ============================================
print("\n" + "="*50)
print("String Analysis:")
print(f"Full string: {city}")
print(f"Length: {len(city)}")
print(f"Character indices:")
for i, char in enumerate(city):
    print(f"  Index {i}: '{char}'")

