# Longest consecutive sequence in O(n) average time

def longest_consecutive(numbers):
    values = set(numbers)
    longest = 0

    for number in values:
        if number - 1 not in values:
            length = 1
            current = number

            while current + 1 in values:
                current += 1
                length += 1

            longest = max(longest, length)

    return longest


print(longest_consecutive([100, 4, 200, 1, 3, 2]))
