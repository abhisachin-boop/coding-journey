# Insertion sort

def insertion_sort(numbers):
    numbers = numbers.copy()

    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1

        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j -= 1

        numbers[j + 1] = key

    return numbers


numbers = [12, 11, 13, 5, 6]
print("Sorted:", insertion_sort(numbers))
