import sys
from collections import deque
input=sys.stdin.readline

def find():
  q=deque([[1,0,0,0]])
  visited[0][0]=0 # wall
  while q:
    cnt,x,y,wall=q.popleft()
    if x==N-1 and y==M-1:
      # print(visited)
      print(cnt)
      exit(0)
    for i in range(4):
      newX=x+xbox[i]
      newY=y+ybox[i]
      if 0<=newX<N and 0<=newY<M:
        if l[newX][newY]=='0' and (visited[newX][newY]==-1 or visited[newX][newY]>wall):
          visited[newX][newY]=wall
          q.append([cnt+1,newX,newY,wall])
        elif l[newX][newY]=='1' and wall+1<=K and (visited[newX][newY]==-1 or visited[newX][newY]>wall+1):
          visited[newX][newY]=wall+1
          q.append([cnt+1,newX,newY,wall+1])
  print(-1)

N,M,K=map(int,input().split())
l=[]
for i in range(N):
  l.append(list(input().rstrip()))

xbox=[-1,1,0,0]
ybox=[0,0,-1,1]
visited=[[-1 for i in range(M)]for j in range(N)]
find()
