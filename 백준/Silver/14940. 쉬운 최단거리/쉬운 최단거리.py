import sys
from collections import deque
input=sys.stdin.readline

n,m=map(int,input().split())
l=[]
q=deque([])
flag2=False
for i in range(n):
  now=list(map(int,input().split()))
  l.append(now)
  if not flag2:
    for j in range(m):
      if now[j]==2:
        q.append([i,j,0])
        startx=i
        starty=j
        flag2=True
        break

xbox=[-1,1,0,0]
ybox=[0,0,-1,1]
visited=[[0 for i in range(m)]for j in range(n)]
while q:
  x,y,cnt=q.popleft()
  if 0<=x<n and 0<=y<m and l[x][y]!=0 and (visited[x][y]==0 or visited[x][y]>cnt):
    visited[x][y]=cnt
    for i in range(4):
      q.append([x+xbox[i],y+ybox[i],cnt+1])

visited[startx][starty]=0
for i in range(n):
  for j in range(m):
    if visited[i][j]==0 and l[i][j]==1:
      visited[i][j]=-1

  for j in range(m):
    print(visited[i][j],end=' ')
  print()

