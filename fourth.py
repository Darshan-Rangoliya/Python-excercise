def fibo_fun(n):
    if n <= 1:
        return n
    else:
        return fibo_fun(n-1)+fibo_fun(n-2)

print(fibo_fun(8))

# recursion with memorisation
cache_store = {0:0,1:1}
num = int(input('Enter number--> '))
def rec_fun_with_momorisation(val):
    if val in cache_store:
        return cache_store[val]
    else:
        cache_store[val] = rec_fun_with_momorisation(val-1)+rec_fun_with_momorisation(val-2)
        return cache_store[val]

print(rec_fun_with_momorisation(num))

# sum of the given list with recursion
Numbers = [23, 44, 5, 67, 1, 1, 2, 4, 5]
sum = 0
def rec_sum(index):
    global sum
    if index == (len(Numbers)):
        return sum
    else:
        sum+=Numbers[index]
        return rec_sum(index+1)

rec_sum(0)
print(sum)