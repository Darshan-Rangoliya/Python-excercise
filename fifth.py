from itertools import combinations

numbers = [9, 4, 8, 10, 2, 4, 8, 3, 14, 4, 8]
n = int(input('Enter the number of which you want sum from list :'))

pairs = set(combinations(numbers,2))
sum_list = [pair for pair in pairs if sum(pair)==n]
final_list = set((tuple(sorted(value)) for value in sum_list))
print(final_list)