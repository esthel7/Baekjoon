import sys
from collections import deque
input=sys.stdin.readline

def make(q,H,N,M):
  hbox=[-1,1,0,0,0,0]
  nbox=[0,0,-1,1,0,0]
  mbox=[0,0,0,0,-1,1]
  while q:
    [h,n,m,cnt]=q.popleft()
    if h<0 or n<0 or m<0 or h>=H or n>=N or m>=M:
      continue
    if (l[h][n][m]!=0 and l[h][n][m]<=cnt) or l[h][n][m]==-1:
      continue
    l[h][n][m]=cnt
    for i in range(6):
      q.append([h+hbox[i],n+nbox[i],m+mbox[i],cnt+1])


M,N,H=map(int,input().split())
l=[]
for i in range(H):
  l.append([])
  for j in range(N):
    l[i].append(list(map(int,input().split())))

go=deque([])
for i in range(H):
  for j in range(N):
    for k in range(M):
      if l[i][j][k]==1:
        l[i][j][k]=0
        go.append([i,j,k,1])

make(go,H,N,M)
breakFlag=False
maximum=0
for i in range(H):
  for j in range(N):
    for k in range(M):
      if l[i][j][k]>=1:
        if maximum<l[i][j][k]:
          maximum=l[i][j][k]
      elif l[i][j][k]==0:
        breakFlag=True
        break
    if breakFlag:
      break
  if breakFlag:
    break

if breakFlag:
  print(-1)
else:
  print(maximum-1)
