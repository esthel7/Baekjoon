import sys
from collections import deque
input=sys.stdin.readline

R,C=map(int,input().split())
l=[]
x=-1
y=-1
visit=[[False for i in range(C)]for j in range(R)]
for i in range(R):
  now=list(input().rstrip())
  for j in range(C):
    if now[j]=='S':
      now[j]='.'
      x=i
      y=j
  l.append(now)

visit[x][y]=True
xbox=[-1,1,0,0]
ybox=[0,0,-1,1]

spread=0
waterVisit=[[False for i in range(C)]for j in range(R)]
q=deque([[x,y,0]])
while q:
  x,y,time=q.popleft()
  if time==spread:
    spread+=1
    water=[]
    for i in range(R):
      for j in range(C):
        if waterVisit[i][j]:
          continue
        if l[i][j]=='*':
          waterVisit[i][j]=True
          for k in range(4):
            newX=i+xbox[k]
            newY=j+ybox[k]
            if 0<=newX<R and 0<=newY<C and l[newX][newY]=='.':
              water.append([newX,newY])
    for newX,newY in water:
      l[newX][newY]='*'

  for i in range(4):
    newX=x+xbox[i]
    newY=y+ybox[i]
    if 0<=newX<R and 0<=newY<C and not visit[newX][newY]:
      visit[newX][newY]=True
      if l[newX][newY]=='.':
        q.append([newX,newY,time+1])
      elif l[newX][newY]=='D':
        print(time+1)
        exit(0)


print('KAKTUS')
