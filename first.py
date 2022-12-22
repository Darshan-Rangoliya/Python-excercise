from functools import reduce
from collections import Counter

print('A. Length of the list')
print('B. Display first 3 numbers')
print('C. Display sum of odd numbers')
print('D. Number of duplicate numbers')
print('E. Display list without duplicate numbers')

# numbers = [i for i in range(10)]

numbers = [2, 4, 5, 2, 12, 44, 5, 1, 2, 3]

print(numbers)

choice = str(input('Enter your choice : '))

if choice == 'a' or choice == 'A':
    print(len(numbers))

elif choice == 'b' or choice == 'B':
    print(numbers[0:3])

elif choice == 'c' or choice == 'C':
    # first creating odd_number list and then printing the sum
    print(sum([odd_num for odd_num in numbers if odd_num % 2 != 0]))

elif choice == 'd' or choice == 'D':
    # first counting all the numbers then adding duplicate numbers into duplicate list
    count_all = Counter(numbers)
    duplicate_list = [item for item in count_all if count_all[item] > 1]
    print('Number of duplicate numbers:', len(duplicate_list))

elif choice == 'e' or choice == 'E':
    newList = [*set(numbers)]
    print(newList)

# other mathods

    # res = []
    # [res.append(x) for x in numbers if x not in res]
    # print(res)

    # res1 = [i for n,i in enumerate(numbers) if i not in numbers[:n]]
    # print(res1)
