names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller','Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White']

name_len_list = [len(name_length) for name_length in names]

unique_length = [*set(name_len_list)]  # here sorted set has created with n repeated value

frq = dict()

for unique_val in unique_length:
    frq[unique_val] = name_len_list.count(unique_val)

frq = sorted(frq.items(), key=lambda x: x[1]) # sorting the dictonary to find least and most frequesnt names

most_frq = frq[-3:]
least_frq = frq[0:3]

most_frq.reverse()

def fun_to_print_frequent_names(frq_list):
    for name_len in frq_list:
        temp = [name for name in names if len(name)==name_len[0]]
        print('{} names of length {}:{}'.format(name_len[1], name_len[0], temp))

print('The three most frequent name lenghts are:')

fun_to_print_frequent_names(most_frq)

print('The three least frequent name lenghts are:')

fun_to_print_frequent_names(least_frq)