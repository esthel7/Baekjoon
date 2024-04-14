import sys
from collections import deque
input=sys.stdin.readline

# 빨간구슬 빼내기

N,M=map(int,input().split())
rx=0
ry=0
bx=0
by=0
l=[]
for i in range(N):
  now=list(input().rstrip())
  for j in range(M):
    if now[j]=='R':
      now[j]='.'
      rx=i
      ry=j
    elif now[j]=='B':
      now[j]='.'
      bx=i
      by=j
  l.append(now)

q=deque([[rx,ry,bx,by,0]])
while q:
  frx,fry,fbx,fby,time=q.popleft()
  time+=1
  if time==11:
    print(-1)
    exit(0)

  # top
  rx=frx
  ry=fry
  bx=fbx
  by=fby
  if rx<=bx: # rx부터 움직이기
    exitflag=False
    while True:
      if l[rx-1][ry]=='O':
        rx-=1
        exitflag=True
        break
      elif l[rx-1][ry]=='.':
        rx-=1
      else:
        break

    continueflag=False
    while True:
      if l[bx-1][by]=='O':
        continueflag=True
        break
      elif bx-1==rx and by==ry:
        break
      elif l[bx-1][by]=='.':
        bx-=1
      else:
        break

    if not continueflag and exitflag:
      print(time)
      exit(0)

  else: # bx부터 움직이기
    continueflag=False
    while True:
      if l[bx-1][by]=='O':
        continueflag=True
        break
      elif l[bx-1][by]=='.':
        bx-=1
      else:
        break

    while True:
      if l[rx-1][ry]=='O':
        print(time)
        exit(0)
      elif rx-1==bx and ry==by:
        break
      elif l[rx-1][ry]=='.':
        rx-=1
      else:
        break

  if not continueflag:
    if rx!=frx or ry!=fry or bx!=fbx or by!=fby:
      q.append([rx,ry,bx,by,time])

  # bottom
  rx=frx
  ry=fry
  bx=fbx
  by=fby
  if rx>=bx: # rx부터 움직이기
    exitflag=False
    while True:
      if l[rx+1][ry]=='O':
        rx+=1
        exitflag=True
        break
      elif l[rx+1][ry]=='.':
        rx+=1
      else:
        break

    continueflag=False
    while True:
      if l[bx+1][by]=='O':
        continueflag=True
        break
      elif bx+1==rx and by==ry:
        break
      elif l[bx+1][by]=='.':
        bx+=1
      else:
        break

    if not continueflag and exitflag:
      print(time)
      exit(0)

  else: # bx부터 움직이기
    continueflag=False
    while True:
      if l[bx+1][by]=='O':
        continueflag=True
        break
      elif l[bx+1][by]=='.':
        bx+=1
      else:
        break

    while True:
      if l[rx+1][ry]=='O':
        print(time)
        exit(0)
      elif rx+1==bx and ry==by:
        break
      elif l[rx+1][ry]=='.':
        rx+=1
      else:
        break

  if not continueflag:
    if rx!=frx or ry!=fry or bx!=fbx or by!=fby:
      q.append([rx,ry,bx,by,time])

  # left
  rx=frx
  ry=fry
  bx=fbx
  by=fby
  if ry<=by: # ry부터 움직이기
    exitflag=False
    while True:
      if l[rx][ry-1]=='O':
        ry-=1
        exitflag=True
        break
      elif l[rx][ry-1]=='.':
        ry-=1
      else:
        break

    continueflag=False
    while True:
      if l[bx][by-1]=='O':
        continueflag=True
        break
      elif bx==rx and by-1==ry:
        break
      elif l[bx][by-1]=='.':
        by-=1
      else:
        break

    if not continueflag and exitflag:
      print(time)
      exit(0)

  else: # by부터 움직이기
    continueflag=False
    while True:
      if l[bx][by-1]=='O':
        continueflag=True
        break
      elif l[bx][by-1]=='.':
        by-=1
      else:
        break

    while True:
      if l[rx][ry-1]=='O':
        print(time)
        exit(0)
      elif rx==bx and ry-1==by:
        break
      elif l[rx][ry-1]=='.':
        ry-=1
      else:
        break

  if not continueflag:
    if rx!=frx or ry!=fry or bx!=fbx or by!=fby:
      q.append([rx,ry,bx,by,time])

  # right
  rx=frx
  ry=fry
  bx=fbx
  by=fby
  if ry>=by: # ry부터 움직이기
    exitflag=False
    while True:
      if l[rx][ry+1]=='O':
        ry+=1
        exitflag=True
        break
      elif l[rx][ry+1]=='.':
        ry+=1
      else:
        break

    continueflag=False
    while True:
      if l[bx][by+1]=='O':
        continueflag=True
        break
      elif bx==rx and by+1==ry:
        break
      elif l[bx][by+1]=='.':
        by+=1
      else:
        break

    if not continueflag and exitflag:
      print(time)
      exit(0)

  else: # by부터 움직이기
    continueflag=False
    while True:
      if l[bx][by+1]=='O':
        continueflag=True
        break
      elif l[bx][by+1]=='.':
        by+=1
      else:
        break

    while True:
      if l[rx][ry+1]=='O':
        print(time)
        exit(0)
      elif rx==bx and ry+1==by:
        break
      elif l[rx][ry+1]=='.':
        ry+=1
      else:
        break

  if not continueflag:
    if rx!=frx or ry!=fry or bx!=fbx or by!=fby:
      q.append([rx,ry,bx,by,time])

print(-1)
