# Check whether an array contains a duplicate

def contains_duplicate(numbers):
    seen = set()

    for number in numbers:
        if number in seen:
            return True
        seen.add(number)

    return False


print(contains_duplicate([1, 2, 3, 1]))
print(contains_duplicate([1, 2, 3, 4]))
