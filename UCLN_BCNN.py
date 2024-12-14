import math

def gcd(a,b):
    while b != 0:
        a,b = b,a%b
    return a
def lmn(a,b):
    return a * b // gcd(a,b)
if __name__ == '__main__':
    x,y = map(int,input().split())
    print(gcd(x,y))
    print(lmn(x,y))