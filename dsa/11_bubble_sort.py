# Bubble sort

def bubble_sort(numbers):
    numbers = numbers.copy()

    for i in range(len(numbers)):
        swapped = False
        for j in range(0, len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True
        if not swapped:
            break

    return numbers


numbers = [64, 34, 25, 12, 22, 11, 90]
print("Sorted:", bubble_sort(numbers))
