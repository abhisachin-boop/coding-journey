# Hashing: count frequency of each element using a dictionary

def frequency_counter(values):
    frequency = {}
    for value in values:
        frequency[value] = frequency.get(value, 0) + 1
    return frequency


values = [1, 2, 2, 3, 1, 2, 4, 3]
print(frequency_counter(values))
