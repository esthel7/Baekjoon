import sys
from collections import deque
input=sys.stdin.readline

def find(x,y):
  global answer
  visit=[[False for i in range(M)]for j in range(N)]
  visit[x][y]=True
  q=deque([[0,x,y]])
  while q:
    cnt,x,y=q.popleft()
    if answer<cnt:
      answer=cnt
    for i in range(4):
      newX=x+xbox[i]
      newY=y+ybox[i]
      if 0<=newX<N and 0<=newY<M and l[newX][newY]=='L' and not visit[newX][newY]:
        visit[newX][newY]=True
        q.append([cnt+1,newX,newY])


N,M=map(int,input().split())
l=[]
for i in range(N):
  l.append(list(input().rstrip()))

xbox=[-1,1,0,0]
ybox=[0,0,-1,1]

answer=0
for i in range(N):
  for j in range(M):
    if l[i][j]=='L':
      find(i,j)

print(answer)
