"""Two Sum: find two indices whose values add up to target."""


def two_sum(nums, target):
    seen = {}

    for i, value in enumerate(nums):
        needed = target - value
        if needed in seen:
            return [seen[needed], i]
        seen[value] = i

    return []


if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target = 9
    print(two_sum(numbers, target))  # [0, 1]
