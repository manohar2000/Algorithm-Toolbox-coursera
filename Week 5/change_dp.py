# Uses python3
import sys
import math
def get_change(m):
    denom = [1, 3, 4]
    mini = [0] + [math.inf]*m
    for i in range(1, m+1):
        for j in denom:
            if i>=j:
                coins = mini[i-j]+1
                if coins < mini[i]:
                    mini[i] = coins
    
    return mini[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
