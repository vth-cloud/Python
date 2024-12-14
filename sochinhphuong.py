import math

def chinhphuong(n):
    can = 0
    can = can + int(math.sqrt(n))
    if can * can == n:
        return True
    return False


if __name__ == '__main__':
    n = int(input())
    if chinhphuong(n):
        print("YES")