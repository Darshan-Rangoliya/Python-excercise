numbers = [11, 5, 6, 1, 3, 8, 9, 10]
num_len = len(numbers)

# bubble sort
for index in range(0,num_len-1):
    for second_index in range(0,num_len-index-1):
        if numbers[second_index] > numbers[second_index+1]:
            numbers[second_index+1],numbers[second_index] = numbers[second_index],numbers[second_index+1]

print(numbers)