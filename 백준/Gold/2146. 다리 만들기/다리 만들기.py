import sys
from collections import deque
input=sys.stdin.readline

def pointRoot(N,x,y,num):
  q=[[x,y]]
  visit[x][y]=True

  while q:
    endsFlag=False
    [x,y]=q.pop()
    l[x][y]=num
    for i in range(4):
      newX=x+xbox[i]
      newY=y+ybox[i]
      if 0<=newX<N and 0<=newY<N and not visit[newX][newY]:
        if l[newX][newY]==1:
          q.append([newX,newY])
          visit[newX][newY]=True
        else:
          if not endsFlag:
            endsFlag=True
            ends.append([x,y,num,0])

def make(N):
  total=0
  for i in range(N):
    for j in range(N):
      if l[i][j]==0:
        continue
      if visit[i][j]:
        continue
      total+=1
      pointRoot(N,i,j,total)

def find(N):
  visit=[[[] for i in range(N)]for j in range(N)]
  while ends:
    [x,y,num,now]=ends.popleft()
    if l[x][y]!=0 and l[x][y]!=num:
      print(now-1)
      return
    for i in range(4):
      newX=x+xbox[i]
      newY=y+ybox[i]
      if 0<=newX<N and 0<=newY<N and num not in visit[newX][newY]:
        visit[newX][newY].append(num)
        ends.append([newX,newY,num,now+1])


N=int(input())
l=[]
for i in range(N):
  l.append(list(map(int,input().split())))

xbox=[-1,1,0,0]
ybox=[0,0,-1,1]
ends=deque([]) # 가장자리 정보들
visit=[[False for i in range(N)]for j in range(N)]
make(N)
find(N)
