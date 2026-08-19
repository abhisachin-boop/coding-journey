# Count the frequency of each element

def count_frequency(numbers):
    frequency = {}
    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1
    return frequency


numbers = [1, 2, 2, 3, 1, 2, 4]
print(count_frequency(numbers))
