import math

n = int(input())

# number of operations required for getting 0, 1, 2,.. , n
ops = [0, 0] + [math.inf]*(n-1)

for i in range(2, n+1):
    tempa, tempb, tempc = [math.inf]*3

    tempa = ops[i-1] + 1 
    if i%2 == 0: tempb = ops[i//2] + 1
    if i%3 == 0: tempc = ops[i//3] + 1
    min_ops = min(tempa, tempb, tempc)
    ops[i] = min_ops

print(ops[n])

# Backtracking the numbers leading to n
nums = [n]
while n!=1:
    if n%3 ==0 and ops[n]-1 == ops[n//3]:
        nums += [n//3]
        n = n//3
    elif n%2 ==0 and ops[n]-1 == ops[n//2]:
        nums += [n//2]
        n = n//2
    else:
        nums += [n-1]
        n = n - 1

print(' '.join([str(i) for i in nums][::-1]))