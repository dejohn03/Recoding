def most_frequent(numbers):
    if len(numbers) == 0:
        return None
    
    counts = {}
    for number in numbers:
        if number in counts:
            counts[number] = counts[number] + 1
        else:
            counts[number] = 1
    best = numbers[0]
    best_count = counts[best] 
    for number in numbers:
        if counts[number] > best_count:
            best = number 
            best_count = counts[number]
    return best          
print(most_frequent([2, 5, 2, 8, 2, 5]))  
print(most_frequent([4, 7, 7, 4]))  
print(most_frequent([]))       