import sys
input=sys.stdin.readline

def findNo(l,x,y,N):
  color=l[x][y]
  q=[[x,y]]
  while q:
    [x,y]=q.pop()
    if x<0 or y<0 or x>=N or y>=N or visitedNo[x][y]:
      continue
    if l[x][y]==color:
      visitedNo[x][y]=True
      q.append([x+1,y])
      q.append([x-1,y])
      q.append([x,y+1])
      q.append([x,y-1])
  return visitedNo

def findYes(l,x,y,N):
  color=l[x][y]
  colors=['R','G']
  if color not in colors:
    colors=['B']
  q=[[x,y]]
  while q:
    [x,y]=q.pop()
    if x<0 or y<0 or x>=N or y>=N or visitedYes[x][y]:
      continue
    if l[x][y] in colors:
      visitedYes[x][y]=True
      q.append([x+1,y])
      q.append([x-1,y])
      q.append([x,y+1])
      q.append([x,y-1])
  return visitedYes


N=int(input())
l=[]
visitedNo=[[False for i in range(N)]for j in range(N)]
visitedYes=[[False for i in range(N)]for j in range(N)]
cntNo=0
cntYes=0
for i in range(N):
  l.append(list(input().rstrip()))

for i in range(N):
  for j in range(N):
    if not visitedNo[i][j]:
      cntNo+=1
      visitedNo=findNo(l,i,j,N)
    if not visitedYes[i][j]:
      cntYes+=1
      visitedYes=findYes(l,i,j,N)

print(cntNo,cntYes)
