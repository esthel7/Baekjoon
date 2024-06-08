import sys
import heapq
input=sys.stdin.readline

W,H=map(int,input().split())
startx=-1
starty=-1
endx=-1
endy=-1
l=[]
for i in range(H):
  now=list(input().rstrip())
  l.append(now)
  for j in range(W):
    if l[i][j]=='C':
      if startx==-1:
        startx=i
        starty=j
      else:
        endx=i
        endy=j

Top=0
Bottom=1
Left=2
Right=3
Last=W*H

visited=[[[Last,Last,Last,Last] for i in range(W)]for j in range(H)] # dir mirror
visited[startx][starty]=[0,0,0,0]

xbox=[-1,1,0,0]
ybox=[0,0,-1,1]
q=[]
for i in range(4):
  newX=startx+xbox[i]
  newY=starty+ybox[i]
  if 0<=newX<H and 0<=newY<W and l[newX][newY]!='*':
    heapq.heappush(q,[0,i,startx,starty])

while q:
  mirror,dir,x,y=heapq.heappop(q)
  if x==endx and y==endy:
    print(mirror)
    break

  if dir==Top and x-1>=0 and l[x-1][y]!='*' and visited[x-1][y][dir]>mirror:
    visited[x-1][y][dir]=mirror
    heapq.heappush(q,[mirror,dir,x-1,y])

  elif dir==Bottom and x+1<H and l[x+1][y]!='*' and visited[x+1][y][dir]>mirror:
    visited[x+1][y][dir]=mirror
    heapq.heappush(q,[mirror,dir,x+1,y])

  elif dir==Left and y-1>=0 and l[x][y-1]!='*' and visited[x][y-1][dir]>mirror:
    visited[x][y-1][dir]=mirror
    heapq.heappush(q,[mirror,dir,x,y-1])

  elif dir==Right and y+1<W and l[x][y+1]!='*' and visited[x][y+1][dir]>mirror:
    visited[x][y+1][dir]=mirror
    heapq.heappush(q,[mirror,dir,x,y+1])


  if dir==Top or dir==Bottom:
    if y-1>=0 and l[x][y-1]!='*' and visited[x][y-1][Left]>mirror+1:
      visited[x][y-1][Left]=mirror+1
      heapq.heappush(q,[mirror+1,Left,x,y-1])
    if y+1<W and l[x][y+1]!='*' and visited[x][y+1][Right]>mirror+1:
      visited[x][y+1][Right]=mirror+1
      heapq.heappush(q,[mirror+1,Right,x,y+1])

  elif dir==Left or dir==Right:
    if x-1>=0 and l[x-1][y]!='*' and visited[x-1][y][Top]>mirror+1:
      visited[x-1][y][Top]=mirror+1
      heapq.heappush(q,[mirror+1,Top,x-1,y])

    if x+1<H and l[x+1][y]!='*' and visited[x+1][y][Bottom]>mirror+1:
      visited[x+1][y][Bottom]=mirror+1
      heapq.heappush(q,[mirror+1,Bottom,x+1,y])
