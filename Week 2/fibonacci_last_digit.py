# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    arr = [0]*61
    arr[0] = 0
    arr[1] = 1
    for i in range(2,60):
        arr[i] = (arr[i-1] + arr[i-2])%10
        
    return arr[n%60]
if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
