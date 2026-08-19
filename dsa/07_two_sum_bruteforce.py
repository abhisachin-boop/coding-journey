# Two Sum: return indices of two values whose sum equals target

def two_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i, j]
    return []


numbers = [2, 7, 11, 15]
print(two_sum(numbers, 9))
