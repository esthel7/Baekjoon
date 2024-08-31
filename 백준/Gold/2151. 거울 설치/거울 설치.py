import sys
from collections import deque
input=sys.stdin.readline

N=int(input())
l=[]
x=-1
y=-1
for i in range(N):
  now=list(input().rstrip())
  if x==-1:
    for j in range(N):
      if now[j]=='#':
        x=i
        y=j
        break
  l.append(now)

xbox=[-1,1,0,0]
ybox=[0,0,-1,1]
top=0
bottom=1
left=2
right=3

visited=[[[2500 for i in range(N)]for j in range(N)]for k in range(4)]

q=deque([])
for i in range(4):
  visited[i][x][y]=0
  newX=x+xbox[i]
  newY=y+ybox[i]
  if 0<=newX<N and 0<=newY<N and l[newX][newY]!='*':
    visited[i][newX][newY]=0
    q.append([newX,newY,i])

answer=2500
while q:
  x,y,dir=q.popleft()
  if l[x][y]=='#':
    answer=min(answer,visited[dir][x][y])
    continue

  if dir==top and x-1>=0 and l[x-1][y]!='*' and visited[dir][x-1][y]>visited[dir][x][y]:
    visited[dir][x-1][y]=visited[dir][x][y]
    q.append([x-1,y,dir])
  elif dir==bottom and x+1<N and l[x+1][y]!='*' and visited[dir][x+1][y]>visited[dir][x][y]:
    visited[dir][x+1][y]=visited[dir][x][y]
    q.append([x+1,y,dir])
  elif dir==left and y-1>=0 and l[x][y-1]!='*' and visited[dir][x][y-1]>visited[dir][x][y]:
    visited[dir][x][y-1]=visited[dir][x][y]
    q.append([x,y-1,dir])
  elif dir==right and y+1<N and l[x][y+1]!='*' and visited[dir][x][y+1]>visited[dir][x][y]:
    visited[dir][x][y+1]=visited[dir][x][y]
    q.append([x,y+1,dir])
  
  if l[x][y]=='!':
    if dir==top or dir==bottom:
      if y-1>=0 and l[x][y-1]!='*' and visited[left][x][y-1]>visited[dir][x][y]+1:
        visited[left][x][y-1]=visited[dir][x][y]+1
        q.append([x,y-1,left])
      if y+1<N and l[x][y+1]!='*' and visited[right][x][y+1]>visited[dir][x][y]+1:
        visited[right][x][y+1]=visited[dir][x][y]+1
        q.append([x,y+1,right])
    else:
      if x-1>=0 and l[x-1][y]!='*' and visited[top][x-1][y]>visited[dir][x][y]+1:
        visited[top][x-1][y]=visited[dir][x][y]+1
        q.append([x-1,y,top])
      if x+1<N and l[x+1][y]!='*' and visited[bottom][x+1][y]>visited[dir][x][y]+1:
        visited[bottom][x+1][y]=visited[dir][x][y]+1
        q.append([x+1,y,bottom])

print(answer)
