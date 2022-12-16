# first pattern

# **_**
# *___*
# _____
# *___*
# **_**

n = 5

for i in range(0,n):
    for j in range(0,n):
        if (i==0 and j==0) or (i==0 and j==n-1) or (i==n-1 and j==0) or (i==n-1 and j ==n-1) or (i==1 and j==0) or (i==1 and j==n-1) or (i==0 and j==1) or (i==0 and j==n-2) or (i==n-2 and j==0) or (i==n-2 and j==n-1) or (i==n-1 and j==1) or (i==n-1 and j==n-2):
            print('*',end='')
        else:
            print('_',end='')
    print()

print()

# second pattern

# __*__
# _***_
# *****
# _***_
# __*__

for i in range(0,n):
    for j in range(0,n):
        if (i==0 and j==0) or (i==0 and j==n-1) or (i==n-1 and j==0) or (i==n-1 and j ==n-1) or (i==1 and j==0) or (i==1 and j==n-1) or (i==0 and j==1) or (i==0 and j==n-2) or (i==n-2 and j==0) or (i==n-2 and j==n-1) or (i==n-1 and j==1) or (i==n-1 and j==n-2):
            print('_',end='')
        else:
            print('*',end='')
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