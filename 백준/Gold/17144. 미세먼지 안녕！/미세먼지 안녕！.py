import sys
from collections import deque
input=sys.stdin.readline

# 확산은 공기청저기가 없고 존재하는 칸으로 상하좌우 확산
# 확산 양은 5로 나눈 몫, 남은 값은 (현재-몫*확산칸)

R,C,T=map(int,input().split())
l=[]
clean=[]
total=0
for i in range(R):
  now=deque(map(int,input().split()))
  l.append(now)

  if now[0]==-1:
    clean.append(i)
    for j in range(1,C):
      total+=now[j]
  else:
    for j in range(C):
      total+=now[j]

xbox=[-1,1,0,0]
ybox=[0,0,-1,1]
for _ in range(T):
  change={}
  for i in range(R):
    for j in range(C):
      if l[i][j]>0:
        now=l[i][j]
        spread=now//5
        cnt=0
        for k in range(4):
          newX=i+xbox[k]
          newY=j+ybox[k]
          if 0<=newX<R and 0<=newY<C:
            if newX in clean and newY==0:
              continue
            if newX in change:
              if newY in change[newX]:
                change[newX][newY]+=spread
              else:
                change[newX][newY]=spread
            else:
              change[newX]={newY:spread}
            cnt+=1
        if i in change:
          if j in change[i]:
            change[i][j]-=spread*cnt
          else:
            change[i][j]=-spread*cnt
        else:
          change[i]={j:-spread*cnt}

  for i in change.keys():
    for j in change[i]:
      l[i][j]+=change[i][j]

  # 공기청정기 위
  left=l[clean[0]].pop()
  l[clean[0]].popleft()
  l[clean[0]].appendleft(0)
  l[clean[0]].appendleft(-1)

  for i in range(clean[0]-1,-1,-1):
    nextLeft=l[i][-1]
    l[i][-1]=left
    left=nextLeft

  last=l[0].pop()
  l[0].append(left)
  l[0].append(last)

  left=l[0].popleft()
  for i in range(1,clean[0]):
    nextLeft=l[i][0]
    l[i][0]=left
    left=nextLeft
  total-=left

  # 공기청저기 아래
  left=l[clean[1]].pop()
  l[clean[1]].popleft()
  l[clean[1]].appendleft(0)
  l[clean[1]].appendleft(-1)

  for i in range(clean[1]+1,R):
    nextLeft=l[i][-1]
    l[i][-1]=left
    left=nextLeft

  last=l[R-1].pop()
  l[R-1].append(left)
  l[R-1].append(last)

  left=l[R-1].popleft()
  for i in range(R-2,clean[1],-1):
    nextLeft=l[i][0]
    l[i][0]=left
    left=nextLeft
  total-=left

print(total)
