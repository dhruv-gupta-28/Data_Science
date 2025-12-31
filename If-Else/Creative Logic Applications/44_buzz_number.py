# 44. Check if a number is a 'buzz' number (ends with 7 or is divisible by 7).

num = int(input("Enter a number: "))

if num % 10 == 7 or num % 7 == 0:
    print(f"{num} is a buzz number.")
else:
    print(f"{num} is not a buzz number.")

