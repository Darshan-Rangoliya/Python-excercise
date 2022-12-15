
print('A. Length of the list')
print('B. Display first 3 numbers')
print('C. Display sum of odd numbers')
print('D. Number of duplicate numbers')
print('E. Display list without duplicate numbers')

# numbers = [i for i in range(10)]

numbers = [1,5,5,5,4,64,453,16,464,31,321,2,21,21,21]

print(numbers)

n = str(input('Enter your choice : '))

if n == 'a' or n == 'A':
    print(len(numbers))
elif n == 'b' or n == 'B':
    print(numbers[0:3])
elif n == 'c' or n == 'C':
    sum = 0
    for i in numbers:
        if i%2!=0:
            sum+=i
    print('sum of odd numbers is ',sum)
elif n == 'd' or n == 'D':
    duplicates = 0
    dup_numbers = []
    for i in numbers:
        if numbers.count(i) > 1:
            if dup_numbers.count(i) == 0:
                duplicates+=1
                dup_numbers.append(i)
        
    print('Total duplication ',duplicates)
    print('Duplicate numbers ',dup_numbers)
elif n == 'e' or n == 'E':
    # newList = [*set(numbers)]
    # print(newList)

    res = []
    [res.append(x) for x in numbers if x not in res]
    print(res)

    res1 = [i for n,i in enumerate(numbers) if i not in numbers[:n]]
    print(res1)