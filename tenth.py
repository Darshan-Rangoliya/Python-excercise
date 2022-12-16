from math import ceil,floor
# first pattern

# **_**
# *___*
# _____
# *___*
# **_**

n = 7

for i in range(1,n):
    if i <= ceil(n/2):
        for k in range(floor(n/2)-i+1,0,-1):
            print('*',end='')
        for j in range(2*i-1):
            print('_',end='')
        for k in range(floor(n/2)-i+1,0,-1):
            print('*',end='')
        print()
for i in range(1,floor(n/2)+1):
    for k in range(i):
        print('*',end='')
    for j in range(n-(i*2)):
        print('_',end='')
    for k in range(i):
        print('*',end='')
    print()

print()

# second pattern

# __*__
# _***_
# *****
# _***_
# __*__

for i in range(1,n):
    if i <= ceil(n/2):
        for k in range(floor(n/2)-i+1,0,-1):
            print('_',end='')
        for j in range(2*i-1):
            print('*',end='')
        for k in range(floor(n/2)-i+1,0,-1):
            print('_',end='')
        print()
for i in range(1,floor(n/2)+1):
    for k in range(i):
        print('_',end='')
    for j in range(n-(i*2)):
        print('*',end='')
    for k in range(i):
        print('_',end='')
    print()

print()

# third pattern

# *
# **
# *_*
# *__*
# *****

for i in range(0,n):
    for j in range(0,i+1):
        if j==0 or i==n-1 or j==i:
            print('*',end='')
        else:
            print('_',end='')
    print()

print()

# fourth pattern

# *****
# *___*
# *___*
# *___*
# *****

for i in range(0,n):
    for j in range(0,n):
        if j==0 or i==n-1 or i==0 or j==n-1:
            print('*',end='')
        else:
            print('_',end='')
    print()

print()

# fifth pattern

# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

cnt = 0
for i in range(1,n+1):
    for j in range(1,i+1):
        cnt+=1
        print(str(cnt)+' ',end='')
    print()