import math
def palin(n):
    rev = 0
    rac = n
    while n != 0:
        rev = rev *10 + n%10
        n//=10
    return rev == rac

if __name__ == '__main__':
    n = int(input())
    print(palin(n))