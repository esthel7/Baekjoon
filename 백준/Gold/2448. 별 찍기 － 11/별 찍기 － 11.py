import sys
from collections import deque
input=sys.stdin.readline

def drawStar(x,y):
  l[x][y]='*'
  l[x+1][y-1]='*'
  l[x+1][y+1]='*'
  for i in range(5):
    l[x+2][y-2+i]='*'

N=int(input())
l=[[' 'for i in range(5*(N//3)+(N//3)-1)]for j in range(N)]

q=deque([[0,(5*(N//3)+(N//3)-1)//2]])
while q:
  [x,y]=q.pop()
  drawStar(x,y)
  nextX=x+3
  if nextX>=N:
    continue
  nextY=y-3
  if q and q[0][0]==nextX and q[0][1]==nextY:
    q.popleft()
  else:
    q.appendleft([nextX,nextY])
  nextY=y+3
  q.appendleft([nextX,nextY])

for i in range(N):
  print(''.join(l[i]))
