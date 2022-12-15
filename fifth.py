Numbers = [9, 4, 8, 10, 2, 4, 8, 3, 14, 4, 8]

print(Numbers.reverse())

n = int(input('Enter the number of which you want sum from list :'))

sum_list = []

for number in Numbers:
    for i in range(len(Numbers)):
        if number + Numbers[i] == n:
            tmp = [number,Numbers[i]]
            if tmp not in sum_list:
                tmp.reverse()
                if tmp not in sum_list:
                    sum_list.append(tmp)


print(sum_list)