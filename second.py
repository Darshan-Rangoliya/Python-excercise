names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller',
         'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White']

l = []

for i in names:
    l.append(len(i))
print(l)

sorted_length = [*set(l)]  # here sorted set has created with n repeated value
frq = dict()

for i in sorted_length:
    frq[i] = l.count(i)

frq = sorted(frq.items(), key=lambda x: x[1])

most_frq = frq[-3:]
least_frq = frq[0:3]

most_frq.reverse()

print('The three most frequent name lenghts are:')

for i in most_frq:
    temp = []
    for j in names:
        if len(j) == i[0]:
            temp.append(j)
    print('{} names of length {}:{}'.format(i[1], i[0], temp))

print('The three least frequent name lenghts are:')

for i in least_frq:
    temp = []
    for j in names:
        if len(j) == i[0]:
            temp.append(j)
    print('{} names of length {}:{}'.format(i[1], i[0], temp))
