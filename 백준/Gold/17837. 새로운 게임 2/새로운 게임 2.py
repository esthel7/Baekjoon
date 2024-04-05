import sys
from collections import deque
input=sys.stdin.readline

# 체스판은 흰, 빨, 파
# 말은 K개, 이동방향 정해져있음
# 1~K까지 말 순서대로 이동, 맨 아래 말만 이동
# 말 4개 쌓이면 게임 종료, 말은 위로 쌓아짐

# 흰색은 그냥 이동
# 빨간색은 이동 후 이동한 말의 순서 반대로
# 파란색은 이동방향 반대로하고 한칸 이동, 이동하려는 칸이 파란색인 경우는 이동 x
# 체스판 벗어나는 경우엔 파란색이랑 같이 취급

# 우좌상하

def blueMoving(x,y,d):
  global t
  if d==1:
    d=2
    info[now[0]][2]=d
    if y-1<0 or (y-1>=0 and l[x][y-1]==2):
      while now:
        item=now.popleft()
        move[x][y].append(item)
      if len(move[x][y])>=4:
        print(t)
        exit(0)
    else:
      moving(x,y,d)
  elif d==2:
    d=1
    info[now[0]][2]=d
    if y+1>=N or (y+1<N and l[x][y+1]==2):
      while now:
        item=now.popleft()
        move[x][y].append(item)
      if len(move[x][y])>=4:
        print(t)
        exit(0)
    else:
      moving(x,y,d)
  elif d==3:
    d=4
    info[now[0]][2]=d
    if x+1>=N or (x+1<N and l[x+1][y]==2):
      while now:
        item=now.popleft()
        move[x][y].append(item)
      if len(move[x][y])>=4:
        print(t)
        exit(0)
    else:
      moving(x,y,d)
  else:
    d=3
    info[now[0]][2]=d
    if x-1<0 or (x-1>=0 and l[x-1][y]==2):
      while now:
        item=now.popleft()
        move[x][y].append(item)
      if len(move[x][y])>=4:
        print(t)
        exit(0)
    else:
      moving(x,y,d)


def moving(x,y,d):
  global t
  if d==1: # right
    if y+1<N:
      if l[x][y+1]==0: # white
        while now:
          item=now.popleft()
          move[x][y+1].append(item)
          info[item][1]=y+1
        if len(move[x][y+1])>=4:
          print(t)
          exit(0)
      elif l[x][y+1]==1: # red
        while now:
          item=now.pop()
          move[x][y+1].append(item)
          info[item][1]=y+1
        if len(move[x][y+1])>=4:
          print(t)
          exit(0)
      else:
        blueMoving(x,y,d)
    else:
      blueMoving(x,y,d)

  elif d==2: # left
    if y-1>=0:
      if l[x][y-1]==0:
        while now:
          item=now.popleft()
          move[x][y-1].append(item)
          info[item][1]=y-1
        if len(move[x][y-1])>=4:
          print(t)
          exit(0)
      elif l[x][y-1]==1: # red
        while now:
          item=now.pop()
          move[x][y-1].append(item)
          info[item][1]=y-1
        if len(move[x][y-1])>=4:
          print(t)
          exit(0)
      else:
        blueMoving(x,y,d)
    else:
      blueMoving(x,y,d)

  elif d==3: # top
    if x-1>=0:
      if l[x-1][y]==0:
        while now:
          item=now.popleft()
          move[x-1][y].append(item)
          info[item][0]=x-1
        if len(move[x-1][y])>=4:
          print(t)
          exit(0)
      elif l[x-1][y]==1: # red
        while now:
          item=now.pop()
          move[x-1][y].append(item)
          info[item][0]=x-1
        if len(move[x-1][y])>=4:
          print(t)
          exit(0)
      else:
        blueMoving(x,y,d)
    else:
      blueMoving(x,y,d)

  else: # bottom
    if x+1<N:
      if l[x+1][y]==0:
        while now:
          item=now.popleft()
          move[x+1][y].append(item)
          info[item][0]=x+1
        if len(move[x+1][y])>=4:
          print(t)
          exit(0)
      elif l[x+1][y]==1: # red
        while now:
          item=now.pop()
          move[x+1][y].append(item)
          info[item][0]=x+1
        if len(move[x+1][y])>=4:
          print(t)
          exit(0)
      else:
        blueMoving(x,y,d)
    else:
      blueMoving(x,y,d)


N,K=map(int,input().split())
l=[]
for i in range(N):
  l.append(list(map(int,input().split())))

info={}
move=[[[] for i in range(N)]for j in range(N)]
for i in range(K):
  x,y,d=map(int,input().split())
  x-=1
  y-=1
  info[i+1]=[x,y,d]
  move[x][y].append(i+1)

for t in range(1,1001):
  for i in range(1,K+1):
    x,y,d=info[i]
    now=deque(move[x][y])

    while now:
      if now[0]==i:
        break
      now.popleft()

    while move[x][y]:
      if move[x][y][-1]==i:
        move[x][y].pop()
        break
      move[x][y].pop()

    moving(x,y,d)

print(-1)
