import sys
input=sys.stdin.readline
from collections import deque

def check(i,j):
    q=deque()
    q.append([i,j])
    visited[i][j]=1
    count=0
    while len(q)>0:
        i,j=q.pop()
        count=count+1
        if i+1<N and l[i+1][j]==1 and visited[i+1][j]==0:
            visited[i+1][j]=1
            q.append([i+1,j])
        if i-1>=0 and l[i-1][j]==1 and visited[i-1][j]==0:
            visited[i-1][j]=1
            q.append([i-1,j])
        if j+1<M and l[i][j+1]==1 and visited[i][j+1]==0:
            visited[i][j+1]=1
            q.append([i,j+1])
        if j-1>=0 and l[i][j-1]==1 and visited[i][j-1]==0:
            visited[i][j-1]=1
            q.append([i,j-1])
    
    total.append(count)


def find():
    while len(list)>0:
        i,j=list.pop()
        if visited[i][j]==0:
            check(i,j)


N,M,K=map(int,input().split())
l=[[0 for i in range(M)]for i in range(N)]
list=deque()
for i in range(K):
    r,c=map(int,input().split())
    l[r-1][c-1]=1
    list.append([r-1,c-1])

visited=[[0 for i in range(M)]for i in range(N)]
total=[]
find()
print(max(total))
