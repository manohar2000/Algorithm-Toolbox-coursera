# Uses python3
import sys

def gcd_naive(a, b):
    if(b == 0):
        return a
        
    else:
        return (gcd_naive(b,a%b))

    

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    a , b = max(a,b) , min(a,b)
    print(gcd_naive(a, b))
