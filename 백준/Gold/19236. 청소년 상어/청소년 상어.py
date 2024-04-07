import sys
from collections import deque
import copy
input=sys.stdin.readline

# 물고기는 번호와 방향을 가지고있음
# 0,0에서 묽고기 먹고 시작

# 물고기는 번호가 작은 순서부터 이동 시작, 한칸 이동, 상어가 없고 벽이 아니면 이동 가능
# 이동 불가능하면 45도 반시계 회전
# 다른 물고기가 있는 칸으로 이동하면 서로 위치를 바꾸는 방식으로 이동

# 물고기 이동 후 상어 이동, 방향쪽으로 여러칸도 이동 가능, 물고기 방향 가짐
# 물고기 있는 칸으로만 이동 가능
# 상어 이동 불가능하면 끝

def change(x,y,changex,changey):
  num=l[x][y]
  changeNum=l[changex][changey]

  if changeNum==0:
    info[num][0]=changex
    info[num][1]=changey
  else:
    prevx,prevy,prevdir=info[num]
    info[num][0]=info[changeNum][0]
    info[num][1]=info[changeNum][1]
    info[changeNum][0]=prevx
    info[changeNum][1]=prevy

  l[x][y]=changeNum
  l[changex][changey]=num


l=[[0 for i in range(4)]for j in range(4)] # num만 저장
info={} # 위치, 방향 저장
for i in range(1,17):
  info[i]=[0,0,0]

for i in range(4):
  now=list(map(int,input().split()))
  for j in range(0,8,2):
    a=now[j]
    b=now[j+1]
    if j==0:
      info[a]=[i,0,b]
      l[i][0]=a
    else:
      info[a]=[i,j//2,b]
      l[i][j//2]=a

answer=l[0][0]
dir=info[l[0][0]][2]
info.pop(l[0][0])
l[0][0]=0

q=deque([[0,0,dir,answer,info,l]])
while q:
  nowx,nowy,nowdir,now,info,l=q.popleft()
  if answer<now:
    answer=now

  for num in info:
    [x,y,dir]=info[num]
    flag=dir
    start=False
    while True:
      dir%=8
      if dir==0:
        dir=8
      info[num][2]=dir

      if start and flag==dir:
        break
      start=True
      if dir==1: # top
        if x-1>=0 and (x-1!=nowx or y!=nowy):
          change(x,y,x-1,y)
          break
        else:
          dir+=1
      elif dir==2: # topleft
        if x-1>=0 and y-1>=0 and (x-1!=nowx or y-1!=nowy):
          change(x,y,x-1,y-1)
          break
        else:
          dir+=1
      elif dir==3: # left
        if y-1>=0 and (x!=nowx or y-1!=nowy):
          change(x,y,x,y-1)
          break
        else:
          dir+=1
      elif dir==4: # bottomleft
        if x+1<4 and y-1>=0 and (x+1!=nowx or y-1!=nowy):
          change(x,y,x+1,y-1)
          break
        else:
          dir+=1
      elif dir==5: # bottom
        if x+1<4 and (x+1!=nowx or y!=nowy):
          change(x,y,x+1,y)
          break
        else:
          dir+=1
      elif dir==6: # bottomright
        if x+1<4 and y+1<4 and (x+1!=nowx or y+1!=nowy):
          change(x,y,x+1,y+1)
          break
        else:
          dir+=1
      elif dir==7: # right
        if y+1<4 and (x!=nowx or y+1!=nowy):
          change(x,y,x,y+1)
          break
        else:
          dir+=1
      else: # topright
        if x-1>=0 and y+1<4 and (x-1!=nowx or y+1!=nowy):
          change(x,y,x-1,y+1)
          break
        else:
          dir+=1

  x=nowx
  y=nowy
  if nowdir==1: # top
    if x-1>=0:
      for i in range(1,4):
        if x-i>=0 and l[x-i][y]!=0:
          newL=list(list(arr)for arr in l)
          newInfo=copy.deepcopy(info)
          nextNum=l[x-i][y]
          newL[info[nextNum][0]][info[nextNum][1]]=0
          newInfo.pop(nextNum)
          # nowx,nowy,nowdir,now,info,l
          q.append([x-i,y,info[nextNum][2],now+nextNum,newInfo,newL])
    else:
      continue
  elif nowdir==2: # topleft
    if x-1>=0 and y-1>=0:
      for i in range(1,4):
        if x-i>=0 and y-i>=0 and l[x-i][y-i]!=0:
          newL=list(list(arr)for arr in l)
          newInfo=copy.deepcopy(info)
          nextNum=l[x-i][y-i]
          newL[info[nextNum][0]][info[nextNum][1]]=0
          newInfo.pop(nextNum)
          # nowx,nowy,nowdir,now,info,l
          q.append([x-i,y-i,info[nextNum][2],now+nextNum,newInfo,newL])
    else:
      continue
  elif nowdir==3: # left
    if y-1>=0:
      for i in range(1,4):
        if y-i>=0 and l[x][y-i]!=0:
          newL=list(list(arr)for arr in l)
          newInfo=copy.deepcopy(info)
          nextNum=l[x][y-i]
          newL[info[nextNum][0]][info[nextNum][1]]=0
          newInfo.pop(nextNum)
          # nowx,nowy,nowdir,now,info,l
          q.append([x,y-i,info[nextNum][2],now+nextNum,newInfo,newL])
    else:
      continue
  elif nowdir==4: # bottomleft
    if x+1<4 and y-1>=0:
      for i in range(1,4):
        if x+i<4 and y-i>=0 and l[x+i][y-i]!=0:
          newL=list(list(arr)for arr in l)
          newInfo=copy.deepcopy(info)
          nextNum=l[x+i][y-i]
          newL[info[nextNum][0]][info[nextNum][1]]=0
          newInfo.pop(nextNum)
          # nowx,nowy,nowdir,now,info,l
          q.append([x+i,y-i,info[nextNum][2],now+nextNum,newInfo,newL])
    else:
      continue
  elif nowdir==5: # bottom
    if x+1<4:
      for i in range(1,4):
        if x+i<4 and l[x+i][y]!=0:
          newL=list(list(arr)for arr in l)
          newInfo=copy.deepcopy(info)
          nextNum=l[x+i][y]
          newL[info[nextNum][0]][info[nextNum][1]]=0
          newInfo.pop(nextNum)
          # nowx,nowy,nowdir,now,info,l
          q.append([x+i,y,info[nextNum][2],now+nextNum,newInfo,newL])
    else:
      continue
  elif nowdir==6: # bottomright
    if x+1<4 and y+1<4:
      for i in range(1,4):
        if x+i<4 and y+i<4 and l[x+i][y+i]!=0:
          newL=list(list(arr)for arr in l)
          newInfo=copy.deepcopy(info)
          nextNum=l[x+i][y+i]
          newL[info[nextNum][0]][info[nextNum][1]]=0
          newInfo.pop(nextNum)
          # nowx,nowy,nowdir,now,info,l
          q.append([x+i,y+i,info[nextNum][2],now+nextNum,newInfo,newL])
    else:
      continue
  elif nowdir==7: # right
    if y+1<4:
      for i in range(1,4):
        if y+i<4 and l[x][y+i]!=0:
          newL=list(list(arr)for arr in l)
          newInfo=copy.deepcopy(info)
          nextNum=l[x][y+i]
          newL[info[nextNum][0]][info[nextNum][1]]=0
          newInfo.pop(nextNum)
          # nowx,nowy,nowdir,now,info,l
          q.append([x,y+i,info[nextNum][2],now+nextNum,newInfo,newL])
    else:
      continue
  else: # topright
    if x-1>=0 and y+1<4:
      for i in range(1,4):
        if x-i>=0 and y+i<4 and l[x-i][y+i]!=0:
          newL=list(list(arr)for arr in l)
          newInfo=copy.deepcopy(info)
          nextNum=l[x-i][y+i]
          newL[info[nextNum][0]][info[nextNum][1]]=0
          newInfo.pop(nextNum)
          # nowx,nowy,nowdir,now,info,l
          q.append([x-i,y+i,info[nextNum][2],now+nextNum,newInfo,newL])
    else:
      continue

print(answer)
