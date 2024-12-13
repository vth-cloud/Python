import math
def Prime(n):
    cnt = 0
    for i in range(2,int(math.sqrt(n))):
        if n%i == 0:
            return False
    return True



if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        if Prime(i):
            print(i,end=" ")