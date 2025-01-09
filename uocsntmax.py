import math
def solve(n):
    ans = -1
    for i in range(2,math.isqrt(n)+1):
        if n%i == 0:
            ans = i
            while n % i == 0:
                n//=i
    if n > 1:
        ans = n
    return ans

if __name__ == "__main__":
    n = int(input())
    print(solve(n))
    pass