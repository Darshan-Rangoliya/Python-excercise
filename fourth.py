def fibo_fun(n):
    if n <= 1:
        return n
    else:
        return fibo_fun(n-1)+fibo_fun(n-2)


print(fibo_fun(8))

# to reduece time complexity

num = int(input('Enter number :'))

cache_store = {1: 1, 2: 1}


def fibo_with_memorization(n):
    if n in cache_store:
        return cache_store[n]
    else:
        cache_store[n] = fibo_with_memorization(n-1) + fibo_with_memorization(n-2)
        return cache_store[n]


for i in range(1, num+1):
    if i == num:
        print(fibo_with_memorization(i))

numbers = [23, 44, 5, 67, 1, 1, 2, 4, 5]

# sum = 0
# def rec_sum(index):
#     global sum
#     if index == (len(numbers)):
#         return sum
#     else:
#         sum+=numbers[index]
#         return rec_sum(index+1)

# rec_sum(0)
# print(sum)

# another way

def rec_sum(index):
    if index < 0:
        return 0
    else:
        return numbers[index]+rec_sum(index-1)


print(rec_sum(len(numbers)-1))
