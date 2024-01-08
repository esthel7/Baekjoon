import sys
from collections import deque
input=sys.stdin.readline

def find(n,nx,ny,mx,my):
  if nx==mx and ny==my:
    return 0

  visited=[[False for i in range(n)]for j in range(n)]
  q=deque([[nx,ny,0]])
  while q:
    [x,y,now]=q.popleft()
    if x<0 or y<0 or x>=n or y>=n or visited[x][y]:
      continue
    if x==mx and y==my:
      return now
    visited[x][y]=True
    q.append([x-2,y+1,now+1])
    q.append([x-2,y-1,now+1])
    q.append([x-1,y+2,now+1])
    q.append([x-1,y-2,now+1])
    q.append([x+2,y+1,now+1])
    q.append([x+2,y-1,now+1])
    q.append([x+1,y+2,now+1])
    q.append([x+1,y-2,now+1])


T=int(input())
for i in range(T):
  n=int(input())
  nowx,nowy=map(int,input().split())
  movex,movey=map(int,input().split())
  print(find(n,nowx,nowy,movex,movey))
