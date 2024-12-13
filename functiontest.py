import math

def demuoc(n):
    cnt = 0
    for i in range(1, int(math.sqrt(n))+1):
        if n%i == 0:
            cnt += 1
            if i != n//i:
                cnt += 1
    return cnt
def tonguoc(n):
    tong = 0
    for i in range(1,int(math.sqrt(n))+1):
        if n%i == 0:
            tong = tong + i
            if i != n//i:
                tong += n//i
    return tong
    
    

if __name__ == '__main__':
    n = int(input())
    print(demuoc(n))
    print(tonguoc(n))