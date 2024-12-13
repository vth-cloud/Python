import math

a,b,n = map(int,input().split())
check = False
for x in range(1,n//a+1):
    temp = n-a*x
    if temp % b == 0:
        #print(x,temp,sep=";")
        check = True
        break
if check:
    print("YES YES YES")
else:
    print("NO NO NO")
7 