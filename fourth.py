def fibo_fun(n):
    if n <= 1:
        return n
    else:
        return fibo_fun(n-1)+fibo_fun(n-2)

print(fibo_fun(8))


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