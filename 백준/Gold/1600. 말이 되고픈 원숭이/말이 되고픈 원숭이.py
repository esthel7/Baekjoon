import sys
from collections import deque
input=sys.stdin.readline

K=int(input())
W,H=map(int,input().split())
l=[]
for i in range(H):
  l.append(list(map(int,input().split())))

visited=[[[0 for i in range(W)]for j in range(H)]for k in range(K+1)]
visited[0][0][0]=1

xbox=[-1,1,0,0]
ybox=[0,0,-1,1]
hxbox=[-2,-2,-1,-1,1,1,2,2]
hybox=[-1,1,-2,2,-2,2,-1,1]

q=deque([[0,0,0,1]])
while q:
  x,y,cnt,move=q.popleft()
  if x==H-1 and y==W-1:
    print(move-1)
    exit(0)

  for i in range(4):
    newX=x+xbox[i]
    newY=y+ybox[i]
    if 0<=newX<H and 0<=newY<W and l[newX][newY]!=1 and visited[cnt][newX][newY]==0:
      visited[cnt][newX][newY]=move+1
      q.append([newX,newY,cnt,move+1])
  if cnt+1<=K:
    for i in range(8):
      newX=x+hxbox[i]
      newY=y+hybox[i]
      if 0<=newX<H and 0<=newY<W and l[newX][newY]!=1 and visited[cnt+1][newX][newY]==0:
        visited[cnt+1][newX][newY]=move+1
        q.append([newX,newY,cnt+1,move+1])

print(-1)
