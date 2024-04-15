import sys
import copy
input=sys.stdin.readline

# 물고기 M마리, 이동방향 있음
# 상어와 물고기가 같은 칸에, 물고기들이 같은 칸에 있을 수 있음

# 모든 물고기 상어 없고 냄새 없고 칸 안쪽으로 한칸 이동, 이동 불가하면 이동 안함, 이동할 수 있을 때까지 45도 반시계 회전
# 상어가 연속 3칸 이동, 상하좌우 인접칸으로 이동, 칸 밖으로 못벗어남
# 상어 이동칸에 있는 모든 물고기는 없어지고 냄새를 남김, 가장 많은 물고기를 없애는 방법으로

# 두번 전 연습에서 생긴 냄새가 사라짐
# 처음 위치에 있던 물고기가 그대로 다시 생김

def saveNewFish(x,y,d,cnt): # 물고기 한 칸 이동
  if x in newFish:
    if y in newFish[x]:
      if d in newFish[x][y]:
        newFish[x][y][d]+=cnt
      else:
        newFish[x][y][d]=cnt
    else:
      newFish[x][y]={d:cnt}
  else:
    newFish[x]={y:{d:cnt}}

def saveRemoveFish(x,y): # 사라질 물고기 기록
  if x in remove:
    remove[x].append(y)
  else:
    remove[x]=[y]

def makeSharkMove(now): 
  if len(now)==3:
    move.append(list(now))
    return
  for i in range(1,5):
    now.append(i)
    makeSharkMove(list(now))
    now.pop()


M,S=map(int,input().split())
l=[[-3 for i in range(4)]for j in range(4)] # 냄새만 보관
fish={} # 물고기 방향과 개수만 보관
for i in range(M):
  x,y,d=map(int,input().split())
  x-=1
  y-=1
  if x in fish:
    if y in fish[x]:
      if d in fish[x][y]:
        fish[x][y][d]+=1
      else:
        fish[x][y][d]=1
    else:
      fish[x][y]={d:1}
  else:
    fish[x]={y:{d:1}}

sharkx,sharky=map(int,input().split())
sharkx-=1
sharky-=1
move=[]
makeSharkMove([])

for time in range(S):
  newFish={}

  for x in fish:
    for y in fish[x]:
      for d in fish[x][y]:
        firstDir=d
        cnt=fish[x][y][d]
        startFlag=False
        while True:
          if startFlag and d==firstDir:
            saveNewFish(x,y,d,cnt)
            break
          startFlag=True
          if d==1: # left
            if y-1>=0 and (sharkx!=x or sharky!=y-1) and l[x][y-1]<=time-3:
              saveNewFish(x,y-1,d,cnt)
              break
            else:
              d=8
          elif d==2: # topleft
            if x-1>=0 and y-1>=0 and (sharkx!=x-1 or sharky!=y-1) and l[x-1][y-1]<=time-3:
              saveNewFish(x-1,y-1,d,cnt)
              break
            else:
              d=1
          elif d==3: # top
            if x-1>=0 and (sharkx!=x-1 or sharky!=y) and l[x-1][y]<=time-3:
              saveNewFish(x-1,y,d,cnt)
              break
            else:
              d=2
          elif d==4: # topright
            if x-1>=0 and y+1<4 and (sharkx!=x-1 or sharky!=y+1) and l[x-1][y+1]<=time-3:
              saveNewFish(x-1,y+1,d,cnt)
              break
            else:
              d=3
          elif d==5: # right
            if y+1<4 and (sharkx!=x or sharky!=y+1) and l[x][y+1]<=time-3:
              saveNewFish(x,y+1,d,cnt)
              break
            else:
              d=4
          elif d==6: # bottomright
            if x+1<4 and y+1<4 and (sharkx!=x+1 or sharky!=y+1) and l[x+1][y+1]<=time-3:
              saveNewFish(x+1,y+1,d,cnt)
              break
            else:
              d=5
          elif d==7: # bottom
            if x+1<4 and (sharkx!=x+1 or sharky!=y) and l[x+1][y]<=time-3:
              saveNewFish(x+1,y,d,cnt)
              break
            else:
              d=6
          else: # bottomleft
            if x+1<4 and y-1>=0 and (sharkx!=x+1 or sharky!=y-1) and l[x+1][y-1]<=time-3:
              saveNewFish(x+1,y-1,d,cnt)
              break
            else:
              d=7

  # top, left, bottom, right
  Max=-1
  removeFish={}
  finalsx=-1
  finslsy=-1
  for i in range(64):
    sx=sharkx
    sy=sharky
    nowFish=copy.deepcopy(newFish)
    remove={}
    cnt=0
    breakflag=False
    for dir in move[i]:
      if dir==1: # top
        if sx-1<0:
          breakflag=True
          break
        if sx-1 in nowFish:
          if sy in nowFish[sx-1]:
            for d in nowFish[sx-1][sy]:
              cnt+=nowFish[sx-1][sy][d]
            nowFish[sx-1].pop(sy)
            saveRemoveFish(sx-1,sy)
        sx-=1
      elif dir==2: # left
        if sy-1<0:
          breakflag=True
          break
        if sx in nowFish:
          if sy-1 in nowFish[sx]:
            for d in nowFish[sx][sy-1]:
              cnt+=nowFish[sx][sy-1][d]
            nowFish[sx].pop(sy-1)
            saveRemoveFish(sx,sy-1)
        sy-=1
      elif dir==3: # bottom
        if sx+1>=4:
          breakflag=True
          break
        if sx+1 in nowFish:
          if sy in nowFish[sx+1]:
            for d in nowFish[sx+1][sy]:
              cnt+=nowFish[sx+1][sy][d]
            nowFish[sx+1].pop(sy)
            saveRemoveFish(sx+1,sy)
        sx+=1
      else: # right
        if sy+1>=4:
          breakflag=True
          break
        if sx in nowFish:
          if sy+1 in nowFish[sx]:
            for d in nowFish[sx][sy+1]:
              cnt+=nowFish[sx][sy+1][d]
            nowFish[sx].pop(sy+1)
            saveRemoveFish(sx,sy+1)
        sy+=1

    if not breakflag and Max<cnt:
      Max=cnt
      removeFish=copy.deepcopy(remove)
      finalsx=sx
      finalsy=sy

  sharkx=finalsx
  sharky=finalsy
  for x in removeFish:
    for y in removeFish[x]:
      newFish[x].pop(y)
      l[x][y]=time

  for x in fish:
    for y in fish[x]:
      for d in fish[x][y]:
        saveNewFish(x,y,d,fish[x][y][d])

  fish=copy.deepcopy(newFish)

answer=0
for x in fish:
  for y in fish[x]:
    for d in fish[x][y]:
      answer+=fish[x][y][d]

print(answer)

# 1 left
# 2 lefttop
# 3 top
# 4 topright
# 5 right
# 6 bottomright
# 7 bottom
# 8 bottomleft 

# 상어, 상좌하우
