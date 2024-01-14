import sys
from collections import deque
input=sys.stdin.readline

def count(n,m,newq):
  # 모두 0이면 -1 return
  if len(newq)==0:
    return -1

  visit=[[False for i in range(m)]for j in range(n)]

  for [x,y] in newq:
    visit[x][y]=True

  cnt=0
  for [x,y] in newq:
    if not visit[x][y]:
      continue
    cnt+=1

    nowq=[[x,y]]
    while nowq:
      [x,y]=nowq.pop()
      if not visit[x][y]:
        continue
      visit[x][y]=False
      for i in range(4):
        nowq.append([x+xbox[i],y+ybox[i]])
  return cnt


def find(n,m,q):
  days=0

  while True:
    days+=1
    newq=deque([])
    countFlag=False

    while q:
      [x,y]=q.popleft()
      if l[0][x][y]==0:
        countFlag=True
        continue

      cnt=0
      for i in range(4):
        newX=x+xbox[i]
        newY=y+ybox[i]
        if l[0][newX][newY]==0:
          cnt+=1

      if cnt!=0:
        l[1][x][y]=cnt
      newq.append([x,y])

    if len(newq)==0: # 남은 빙산
      return 0

    if countFlag:
      num=count(n,m,newq)
      if num>=2:
        return days-1

    q=newq

    for [x,y] in q:
      l[0][x][y]-=l[1][x][y]
      l[1][x][y]=0
      if l[0][x][y]<0:
        l[0][x][y]=0


n,m=map(int,input().split())
l=[[],[]]
for i in range(n):
  l[0].append(list(map(int,input().split())))
  l[1].append([0 for j in range(m)])

q=deque([])
for i in range(n):
  for j in range(m):
    if l[0][i][j]>0:
      q.append([i,j])

xbox=[-1,1,0,0]
ybox=[0,0,-1,1]

print(find(n,m,q))
