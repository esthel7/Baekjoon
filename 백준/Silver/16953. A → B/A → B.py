import sys
input=sys.stdin.readline

A,B=map(int,input().split())

count=1
while A<B:
    if B%2==0:
        count=count+1
        B=B/2
    else:
        if B%10==1:
            count=count+1
            B=B//10
        else:
            break

if A==B:
    print(count)
else:
    print(-1)
