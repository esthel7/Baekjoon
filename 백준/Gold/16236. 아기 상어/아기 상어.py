import sys
from collections import deque
input=sys.stdin.readline

# 크기가 큰 물고기있으면 못지나감
# 크기가 작으면 먹을 수 있음 (가장 가까운 물고기, 가장 위 & 왼쪽)
# 크기만큼 물고기 개수를 먹으면 1 커짐

N=int(input())
l=[]
fish=[]
sharkx=-1
sharky=-1

for i in range(N):
  now=list(map(int,input().split()))
  l.append(now)
  for j in range(N):
    if now[j]==9:
      sharkx=i
      sharky=j
    elif now[j]!=0:
      fish.append([i,j])

xbox=[-1,0,0,1]
ybox=[0,-1,1,0]

shark=2
eat=0
answer=0
cnt=0

while True:
  visit=[[False for i in range(N)]for j in range(N)]
  eatable=[] # 먹을 후보의 물고기
  eatableCnt=-1 # 먹을 물고기 거리

  l[sharkx][sharky]=0
  visit[sharkx][sharky]=True
  q=deque([[sharkx,sharky,cnt]])

  while q:
    [x,y,cnt]=q.popleft()
    if eatableCnt!=-1 and eatableCnt==cnt:
      break

    for i in range(4):
      newX=x+xbox[i]
      newY=y+ybox[i]
      if 0<=newX<N and 0<=newY<N and not visit[newX][newY]:
        if l[newX][newY]!=0:
          if l[newX][newY]<shark:
            eatable.append([newX,newY])
            eatableCnt=cnt+1
            answer=cnt+1
          elif l[newX][newY]==shark:
            q.append([newX,newY,cnt+1])
        else:
          q.append([newX,newY,cnt+1])
        visit[newX][newY]=True

  if not eatable:
    print(answer)
    break

  eatable.sort()
  eat+=1
  if eat==shark:
    shark+=1
    eat=0
  l[eatable[0][0]][eatable[0][1]]=0
  sharkx=eatable[0][0]
  sharky=eatable[0][1]
  cnt=answer

