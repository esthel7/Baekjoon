import sys
from collections import deque
input=sys.stdin.readline

def find():
    q=deque()
    q.append((0,0))
    l[0][0]=2
    while len(q)>0:
        n,m=q.popleft()
        if n==N-1 and m==M-1:
            print(l[n][m]-1)
            break
        if n+1<N and l[n+1][m]==1:
            l[n+1][m]=l[n][m]+1
            q.append((n+1,m))
        if m+1<M and l[n][m+1]==1:
            l[n][m+1]=l[n][m]+1
            q.append((n,m+1))
        if n-1>=0 and l[n-1][m]==1:
            l[n-1][m]=l[n][m]+1
            q.append((n-1,m))
        if m-1>=0 and l[n][m-1]==1:
            l[n][m-1]=l[n][m]+1
            q.append((n,m-1))


N,M=map(int,input().split())
l=[0 for i in range(N)]
for i in range(N):
    l[i]=list(map(int,input().rstrip()))

find()
