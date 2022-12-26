from math import ceil, floor
n = int(input('Enter number: '))

# first pattern
# **_**
# *___*
# _____
# *___*
# **_**
for index in range(0, n):
    star = abs(floor((n/2) - index)) % (n-1)
    space = n - 2*(abs(floor((n/2) - index)) % (n-1))
    print('*'*star, end='')
    print('_'*space, end='')
    print('*'*star, end='')
    print()

print()

# second pattern
# __*__
# _***_
# *****
# _***_
# __*__
for index in range(0, n):
    star = abs(floor((n/2) - index)) % (n-1)
    space = n - 2*(abs(floor((n/2) - index)) % (n-1))
    print('_'*star, end='')
    print('*'*space, end='')
    print('_'*star, end='')
    print()

print()

# third pattern
# *
# **
# *_*
# *__*
# *****
for i in range(0, n):
    for j in range(0, i+1):
        if j == 0 or i == n-1 or j == i:
            print('*', end='')
        else:
            print('_', end='')
    print()

print()

# fourth pattern
# *****
# *___*
# *___*
# *___*
# *****
for i in range(0, n):
    for j in range(0, n):
        if j == 0 or i == n-1 or i == 0 or j == n-1:
            print('*', end='')
        else:
            print('_', end='')
    print()

print()

# fifth pattern
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
cnt = 0
for i in range(1, n+1):
    for j in range(1, i+1):
        cnt += 1
        print(str(cnt)+' ', end='')
    print()
