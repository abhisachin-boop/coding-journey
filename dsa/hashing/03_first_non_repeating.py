# Find the first non-repeating character in a string

def first_non_repeating(text):
    frequency = {}

    for char in text:
        frequency[char] = frequency.get(char, 0) + 1

    for char in text:
        if frequency[char] == 1:
            return char

    return None


print(first_non_repeating("aabbcdde"))
