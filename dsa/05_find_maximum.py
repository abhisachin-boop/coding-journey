# Find the maximum element without using max()

def find_maximum(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")

    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    return largest


numbers = [12, 45, 7, 89, 34]
print("Maximum:", find_maximum(numbers))
