# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    
    l = get_majority_element(a, left, (left + right - 1) // 2 + 1)
    r = get_majority_element(a, (left + right - 1) // 2 + 1, right)

    lc = 0
    for i in range(left, right):
        if a[i] == l:
            lc += 1
    if lc > (right - left) // 2:
        return l

    rc = 0
    for i in range(left, right):
        if a[i] == r:
            rc += 1
    if rc > (right - left) // 2:
        return r
    
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
