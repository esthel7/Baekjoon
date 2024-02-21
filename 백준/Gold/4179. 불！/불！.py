import sys
from collections import deque
input=sys.stdin.readline

R,C=map(int,input().split())
l=[]
for i in range(R):
  l.append(list(input().rstrip()))

visited=[[False for i in range(C)]for j in range(R)]
person=deque([])
fire=deque([])
for i in range(R):
  for j in range(C):
    if l[i][j]=='J':
      l[i][j]='.'
      visited[i][j]=True
      person.append([i,j,0])
    elif l[i][j]=='F':
      fire.append([i,j,0])

xbox=[-1,1,0,0]
ybox=[0,0,-1,1]

while True:
  first=person[0][2]
  while fire:
    if fire[0][2]!=first:
      break
    [fx,fy,cnt]=fire.popleft()
    for i in range(4):
      newFx=fx+xbox[i]
      newFy=fy+ybox[i]
      if 0<=newFx<R and 0<=newFy<C:
        if l[newFx][newFy]=='.':
          l[newFx][newFy]='F'
          fire.append([newFx,newFy,cnt+1])

  while person:
    if person[0][2]!=first:
      break
    [x,y,cnt]=person.popleft()
    for i in range(4):
      newX=x+xbox[i]
      newY=y+ybox[i]
      if 0<=newX<R and 0<=newY<C:
        if l[newX][newY]=='.' and not visited[newX][newY]:
          visited[newX][newY]=True
          person.append([newX,newY,cnt+1])
      else:
        print(cnt+1)
        exit(0)
  if not person:
    print('IMPOSSIBLE')
    break
