import sys
input=sys.stdin.readline

def find():
    total=0
    cnt=[0 for i in range(10**5+1)]
    n=N
    s=[]
    s.append((n,0))
    cnt[n]=1
    while len(s)>0:
        n,total=s.pop(0)
        total=total+1
        if n==K:
            print(total-1)
            break
        if n+1<=100000:
            if cnt[n+1]==0:
                s.append((n+1,total))
                cnt[n+1]=1
        if n-1>=0:
            if cnt[n-1]==0:
                s.append((n-1,total))
            cnt[n-1]=1
        if 2*n<2*K and 2*n<=100000:
            if cnt[2*n]==0:
                s.append((2*n,total))
                cnt[2*n]=1

# N은 하나씩 증감 혹은 2배로 증가
N,K=map(int,input().split())

find()
