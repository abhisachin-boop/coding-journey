# Two Sum optimized with a hash map

def two_sum(numbers, target):
    seen = {}

    for index, value in enumerate(numbers):
        complement = target - value
        if complement in seen:
            return [seen[complement], index]
        seen[value] = index

    return []


numbers = [2, 7, 11, 15]
print(two_sum(numbers, 9))
