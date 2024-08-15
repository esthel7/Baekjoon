import sys
from collections import deque
input=sys.stdin.readline

East=1
West=2
South=3
North=4

M,N=map(int,input().split())
visited=[[[False for i in range(4)] for i in range(N)]for j in range(M)]
l=[]
for i in range(M):
  l.append(list(map(int,input().split())))

nowx,nowy,nowdir=map(int,input().split())
tx,ty,tdir=map(int,input().split())
nowx-=1
nowy-=1
tx-=1
ty-=1

q=deque([[nowx,nowy,nowdir,0]])
visited[nowx][nowy][nowdir-1]=True
while q:
  x,y,dir,cnt=q.popleft()
  if x==tx and y==ty and dir==tdir:
    print(cnt)
    exit(0)
  if dir==East:
    if y+1<N and l[x][y+1]==0:
      if not visited[x][y+1][dir-1]:
        visited[x][y+1][dir-1]=True
        q.append([x,y+1,dir,cnt+1])
      if y+2<N and l[x][y+2]==0:
        if not visited[x][y+2][dir-1]:
          visited[x][y+2][dir-1]=True
          q.append([x,y+2,dir,cnt+1])
        if y+3<N and l[x][y+3]==0:
          if not visited[x][y+3][dir-1]:
            visited[x][y+3][dir-1]=True
            q.append([x,y+3,dir,cnt+1])
    if not visited[x][y][South-1]:
      visited[x][y][South-1]=True
      q.append([x,y,South,cnt+1])
    if not visited[x][y][North-1]:
      visited[x][y][North-1]=True
      q.append([x,y,North,cnt+1])
  elif dir==West:
    if y-1>=0 and l[x][y-1]==0:
      if not visited[x][y-1][dir-1]:
        visited[x][y-1][dir-1]=True
        q.append([x,y-1,dir,cnt+1])
      if y-2>=0 and l[x][y-2]==0:
        if not visited[x][y-2][dir-1]:
          visited[x][y-2][dir-1]=True
          q.append([x,y-2,dir,cnt+1])
        if y-3>=0 and l[x][y-3]==0:
          if not visited[x][y-3][dir-1]:
            visited[x][y-3][dir-1]=True
            q.append([x,y-3,dir,cnt+1])
    if not visited[x][y][South-1]:
      visited[x][y][South-1]=True
      q.append([x,y,South,cnt+1])
    if not visited[x][y][North-1]:
      visited[x][y][North-1]=True
      q.append([x,y,North,cnt+1])
  elif dir==South:
    if x+1<M and l[x+1][y]==0:
      if not visited[x+1][y][dir-1]:
        visited[x+1][y][dir-1]=True
        q.append([x+1,y,dir,cnt+1])
      if x+2<M and l[x+2][y]==0:
        if not visited[x+2][y][dir-1]:
          visited[x+2][y][dir-1]=True
          q.append([x+2,y,dir,cnt+1])
        if x+3<M and l[x+3][y]==0:
          if not visited[x+3][y][dir-1]:
            visited[x+3][y][dir-1]=True
            q.append([x+3,y,dir,cnt+1])
    if not visited[x][y][East-1]:
      visited[x][y][East-1]=True
      q.append([x,y,East,cnt+1])
    if not visited[x][y][West-1]:
      visited[x][y][West-1]=True
      q.append([x,y,West,cnt+1])
  else:
    if x-1>=0 and l[x-1][y]==0:
      if not visited[x-1][y][dir-1]:
        visited[x-1][y][dir-1]=True
        q.append([x-1,y,dir,cnt+1])
      if x-2>=0 and l[x-2][y]==0:
        if not visited[x-2][y][dir-1]:
          visited[x-2][y][dir-1]=True
          q.append([x-2,y,dir,cnt+1])
        if x-3>=0 and l[x-3][y]==0:
          if not visited[x-3][y][dir-1]:
            visited[x-3][y][dir-1]=True
            q.append([x-3,y,dir,cnt+1])
    if not visited[x][y][East-1]:
      visited[x][y][East-1]=True
      q.append([x,y,East,cnt+1])
    if not visited[x][y][West-1]:
      visited[x][y][West-1]=True
      q.append([x,y,West,cnt+1])
