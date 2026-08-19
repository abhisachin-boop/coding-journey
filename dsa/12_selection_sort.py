# Selection sort

def selection_sort(numbers):
    numbers = numbers.copy()

    for i in range(len(numbers)):
        minimum_index = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[minimum_index]:
                minimum_index = j
        numbers[i], numbers[minimum_index] = numbers[minimum_index], numbers[i]

    return numbers


numbers = [64, 25, 12, 22, 11]
print("Sorted:", selection_sort(numbers))
