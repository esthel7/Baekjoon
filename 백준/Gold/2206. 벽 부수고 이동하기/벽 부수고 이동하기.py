import sys
from collections import deque
input=sys.stdin.readline

def find(N,M):
  nbox=[-1,1,0,0]
  mbox=[0,0,-1,1]
  q=deque([[0,0,0,1]])
  while q:
    [z,n,m,cnt]=q.popleft()
    if n==N-1 and m==M-1:
      return cnt

    if z==1: # 벽 이미 부숨
      if first[n][m]==-1 or l[z][n][m]<=cnt:
        continue
    else:
      if first[n][m]==0:
        if l[z][n][m]<=cnt:
          continue
      else: # 처음 벽 만남
        z=1
        if l[z][n][m]<=cnt:
          continue

    l[z][n][m]=cnt
    for i in range(4):
      newN=n+nbox[i]
      newM=m+mbox[i]
      if 0<=newN<N and 0<=newM<M:
        q.append([z,newN,newM,cnt+1])
  return -1


N,M=map(int,input().split())
first=[]
for i in range(N):
  first.append(list(input().rstrip()))

l=[[[0 for i in range(M)]for j in range(N)]for k in range(2)] # 0은 보존, 1은 부숨
for i in range(N):
  for j in range(M):
    if first[i][j]=='0':
      first[i][j]=0
    else:
      first[i][j]=-1
    l[0][i][j]=2000000
    l[1][i][j]=2000000

print(find(N,M))
