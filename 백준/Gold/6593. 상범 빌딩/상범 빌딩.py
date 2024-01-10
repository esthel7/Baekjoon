import sys
from collections import deque
input=sys.stdin.readline

def make(L,R,C):
  for i in range(L):
    for j in range(R):
      for k in range(C):
        if l[i][j][k]=='S':
          l[i][j][k]='.'
          start[0]=i
          start[1]=j
          start[2]=k

def find(L,R,C):
  zbox=[-1,1,0,0,0,0]
  xbox=[0,0,-1,1,0,0]
  ybox=[0,0,0,0,-1,1]
  q=deque([[start[0],start[1],start[2],0]])
  while q:
    [z,x,y,cnt]=q.popleft()
    if z<0 or x<0 or y<0 or z>=L or x>=R or y>=C:
      continue
    if l[z][x][y]=='#' or visit[z][x][y]<=cnt:
      continue
    if l[z][x][y]=='E':
      print('Escaped in %d minute(s).'%cnt)
      return
    visit[z][x][y]=cnt
    for i in range(6):
      q.append([z+zbox[i],x+xbox[i],y+ybox[i],cnt+1])

  print('Trapped!')


while True:
  L,R,C=map(int,input().split())
  if L==0 and R==0 and C==0:
    break
  l=[]
  start=[0,0,0]
  visit=[[[1000 for i in range(C)]for j in range(R)]for k in range(L)]
  for i in range(L):
    l.append([])
    for j in range(R):
      l[i].append(list(input().rstrip()))
    input()
  make(L,R,C)
  find(L,R,C)

