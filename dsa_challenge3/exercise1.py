def two_sum(numbers, target):
    seen = {}

    for i in range(len(numbers,)):
        needed = target - numbers[i]
                

        if needed in seen:
            return [seen[needed], i]

        seen[numbers[i]] = i

    return None

print(two_sum([2, 7, 11, 15], 9)) 
    