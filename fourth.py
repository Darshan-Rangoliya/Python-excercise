def fibo_fun(n):
    if n <= 1:
        return n
    else:
        return fibo_fun(n-1)+fibo_fun(n-2)

print(fibo_fun(8))

# to reduece time complexity

cache_store = {0:1,1:1}

def fibo_fun_witch_cache(n):
    if n in {0,1}:
        return cache_store[n]
    else:
        cache_store[n] = fibo_fun_witch_cache(n-1)+fibo_fun_witch_cache(n-2)
        return cache_store[n]

fibo_nums = [fibo_fun_witch_cache(n) for n in range(8)]

print(fibo_nums[-1])

numbers = [23, 44, 5, 67, 1, 1, 2, 4, 5]
sum = 0
def rec_sum(index):
    global sum
    if index == (len(numbers)):
        return sum
    else:
        sum+=numbers[index]
        return rec_sum(index+1)

rec_sum(0)
print(sum)