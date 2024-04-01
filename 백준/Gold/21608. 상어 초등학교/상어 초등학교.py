import sys
from collections import deque
input=sys.stdin.readline

# 비어있는 칸 중에서 좋아하는 학생이 인접한 칸이 가장 많은 칸
# 인접한 칸 중에 비어있는 칸이 가장 많은 칸
# 가장 위에, 가장 왼쪽

N=int(input())
l=[[0 for i in range(N)]for j in range(N)]
info={}
for i in range(N**2):
  now=deque(map(int,input().split()))
  num=now.popleft()
  info[num]=now

xbox=[-1,1,0,0]
ybox=[0,0,-1,1]

for idx in info.keys():
  likes=-1
  empty=-1
  x=N
  y=N
  for i in range(N):
    for j in range(N):
      if l[i][j]==0:
        nowLikes=0
        nowEmpty=0
        for k in range(4):
          newI=i+xbox[k]
          newJ=j+ybox[k]
          if 0<=newI<N and 0<=newJ<N:
            if l[newI][newJ] in info[idx]:
              nowLikes+=1
            elif l[newI][newJ]==0:
              nowEmpty+=1
        if nowLikes>likes:
          likes=nowLikes
          empty=nowEmpty
          x=i
          y=j
        elif nowLikes==likes and nowEmpty>empty:
          empty=nowEmpty
          x=i
          y=j
  l[x][y]=idx

answer=0
for i in range(N):
  for j in range(N):
    idx=l[i][j]
    cnt=0
    for k in range(4):
      newI=i+xbox[k]
      newJ=j+ybox[k]
      if 0<=newI<N and 0<=newJ<N and l[newI][newJ] in info[idx]:
        cnt+=1
    if cnt==1:
      answer+=1
    elif cnt==2:
      answer+=10
    elif cnt==3:
      answer+=100
    elif cnt==4:
      answer+=1000

print(answer)
