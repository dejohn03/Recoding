def longest_consecutive(numbers):
    num_set = set(numbers)
    longest = 0

    for number in num_set:
        if number -1 not in num_set:
            current = number
            length = 1

        while current + 1 in num_set:
            current = current + 1
            length = length + 1

        if length > longest:
            longest = length

    return longest
print(longest_consecutive([100, 4, 200, 1, 3, 2]))                    
