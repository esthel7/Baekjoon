import sys
from collections import deque
input=sys.stdin.readline

def find(l,q,N,M):
  nbox=[-1,1,0,0]
  mbox=[0,0,-1,1]

  while q:
    [n,m]=q.popleft()
    for i in range(4):
      x=n+nbox[i]
      y=m+mbox[i]
      if 0<=x<N and 0<=y<M:
        if l[x][y]==-1 or l[x][y]==1:
          continue
        if l[x][y]==0 or (l[x][y]!=0 and l[x][y]>l[n][m]+1):
          l[x][y]=l[n][m]+1
          q.append([x,y])


M,N=map(int,input().split())
l=[]
for i in range(N):
  l.append(list(map(int,input().split())))

go=deque()
for i in range(N):
  for j in range(M):
    if l[i][j]==1:
      go.append([i,j])

find(l,go,N,M)
errorFlag=False
maximum=0
for i in range(N):
  for j in range(M):
    if l[i][j]==0:
      print(-1)
      errorFlag=True
      break
    if maximum<l[i][j]:
      maximum=l[i][j]
  if errorFlag:
    break
if not errorFlag:
  print(maximum-1)
