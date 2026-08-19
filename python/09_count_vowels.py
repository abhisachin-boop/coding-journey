# Count vowels in a string

text = input("Enter text: ")
vowels = "aeiou"
count = sum(1 for char in text.lower() if char in vowels)

print("Vowel count:", count)
