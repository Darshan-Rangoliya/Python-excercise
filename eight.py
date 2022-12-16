numbers = [11, 5, 6, 1, 3, 8, 9, 10]

l = len(numbers)

# bubble sort

for i in range(0,l-1):
    for j in range(0,l-i-1):
        if numbers[j] > numbers[j+1]:
            numbers[j+1],numbers[j] = numbers[j],numbers[j+1]

print(numbers)