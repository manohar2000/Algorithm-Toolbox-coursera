# Uses python3
import sys
def gcd_naive(a, b):
    if(b == 0):
        return a
        
    else:
        return (gcd_naive(b,a%b))

def lcm_naive(a, b):
    if(a%b==0):
        return a
    
    else:
        return  (a*b)//gcd_naive(a,b)
        
    

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    a , b = max(a,b) , min(a,b)
    print(lcm_naive(a, b))

