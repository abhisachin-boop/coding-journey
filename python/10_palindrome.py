# Check whether a string is a palindrome

text = input("Enter text: ").strip().lower()
cleaned = "".join(char for char in text if char.isalnum())

if cleaned == cleaned[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
