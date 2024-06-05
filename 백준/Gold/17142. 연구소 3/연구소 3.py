import sys
from collections import deque
input=sys.stdin.readline

def find(now):
  global answer
  left=L
  visited=[[False for i in range(N)]for j in range(N)]
  q=deque([])
  for [x,y] in now:
    visited[x][y]=True
    q.append([x,y,0])
  time=0

  while q:
    x,y,cnt=q.popleft()
    for i in range(4):
      newX=x+xbox[i]
      newY=y+ybox[i]
      if 0<=newX<N and 0<=newY<N and not visited[newX][newY]:
        visited[newX][newY]=True
        if l[newX][newY]==1:
          continue
        if l[newX][newY]==0:
          left-=1
          time=cnt+1
        q.append([newX,newY,cnt+1])
        if not left:
          break
    if not left:
      break

  if not left:
    if answer==-1 or answer>time:
      answer=time



def make(now,start):
  if len(now)==M:
    find(now)
    return
  for i in range(start,V):
    now.append(virus[i])
    make(now,i+1)
    now.pop()


N,M=map(int,input().split())
l=[]
for i in range(N):
  l.append(list(map(int,input().split())))

virus=[]
L=0
for i in range(N):
  for j in range(N):
    if l[i][j]==2:
      virus.append([i,j])
    elif l[i][j]==0:
      L+=1

answer=-1
xbox=[-1,1,0,0]
ybox=[0,0,-1,1]
V=len(virus)
make([],0)
print(answer)
