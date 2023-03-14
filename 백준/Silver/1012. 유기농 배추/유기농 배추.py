import sys
input=sys.stdin.readline

def make(u):
    for i in range(K):
        x,y=l[i]
        u[y][x]=1

def find(u):
    total=0 # 배추
    cnt=0 # 지렁이
    a=0
    b=0
    yes=[]
    no=[]
    if u[a][b]==0:
        no.append((a,b+1))
        no.append((a+1,b))
    else:
        yes.append((a,b+1))
        yes.append((a+1,b))
        total=total+1
        cnt=cnt+1
    visited[a][b]=1

    while total!=K:
        flag=0
        if len(yes)>0:
            a,b=yes.pop(0)
            flag=1
        else:
            a,b=no.pop(0)
        
        if a<N and b<M and a>=0 and b>=0 and visited[a][b]!=1:
            if u[a][b]==1:
                total=total+1
                if flag==0:
                    cnt=cnt+1
                yes.append((a,b-1))
                yes.append((a-1,b))
                yes.append((a,b+1))
                yes.append((a+1,b))
            else:
                no.append((a,b-1))
                no.append((a-1,b))
                no.append((a,b+1))
                no.append((a+1,b))

            visited[a][b]=1
    print(cnt)


T=int(input())
for _ in range(T):
    M,N,K=map(int,input().split())
    l=[]
    for i in range(K):
        x,y=map(int,input().split())
        l.append((x,y))
    u=[[0 for a in range(M)]for b in range(N)]
    visited=[[0 for a in range(M)]for b in range(N)]
    make(u)
    find(u)
