import sys
from collections import deque
input=sys.stdin.readline

l=[]
walls=[]
wall={}
for i in range(8):
  wall[i]={}

for i in range(8):
  now=list(input().rstrip())
  for j in range(8):
    if now[j]=='#':
      walls.append([i,j])
  l.append(now)

for i in range(8):
  if not walls:
    break
  newWalls=[]
  for [x,y] in walls:
    if x in wall[i]:
      wall[i][x][y]=True
    else:
      wall[i][x]={y:True}
    if x+1<8:
      newWalls.append([x+1,y])
  walls=list(newWalls)

xbox=[0,-1,1,0,0,-1,-1,1,1]
ybox=[0,0,0,-1,1,1,-1,1,-1]

visited=[[-1 for i in range(8)]for j in range(8)]
visited[7][7]=0
q=deque([[7,0,0]])
while q:
  x,y,time=q.popleft()
  if x==0 and y==7:
    print(1)
    exit(0)
  for i in range(9):
    newX=x+xbox[i]
    newY=y+ybox[i]
    if 0<=newX<8 and 0<=newY<8 and visited[newX][newY]!=time+1:
      visited[newX][newY]=time+1
      if time+1>=8:
        q.append([newX,newY,time+1])
        continue
      if (newX in wall[time] and newY in wall[time][newX]) or (newX in wall[time+1] and newY in wall[time+1][newX]):
        continue
      q.append([newX,newY,time+1])

print(0)
