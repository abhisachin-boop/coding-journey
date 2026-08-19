# Reverse an array/list without using reverse()

def reverse_array(numbers):
    result = []
    for i in range(len(numbers) - 1, -1, -1):
        result.append(numbers[i])
    return result


numbers = [1, 2, 3, 4, 5]
print("Original:", numbers)
print("Reversed:", reverse_array(numbers))
