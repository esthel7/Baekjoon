import sys
import heapq
input=sys.stdin.readline

# 턴 한번은 1~K까지 모두 옮기기
# 이동할 때 위에 올려져 있는 말도 같이 이동
# 가장 아래에 있는 말만 이동 가능
# 4개 이상 쌓이면 게임 종료

# 흰색은 기존 말 위에 쌓기
# 빨강은 옮기는 말 순서 바꿔서 쌓기
# 파랑은 방향 반대로 하고 한칸 이동 (이동할 칸이 파랑이라면 이동하지 않고 방향만 바꾸기)
# 벗어날 경우 파랑처럼 행동

N,K=map(int,input().split())
l=[]
for i in range(N):
  l.append(list(map(int,input().split())))

board=[[[] for i in range(N)]for j in range(N)]
info={}
for i in range(K):
  x,y,d=map(int,input().split())
  board[x-1][y-1].append([i,d]) # idx, dir
  info[i]=[x-1,y-1,d,True]

def WhiteRedChange(idx,x,y,d,tops):
  global endFlag
  if l[x][y]==0: # white
    if len(board[x][y]):
      info.pop(idx)
    else:
      info[idx]=[x,y,d,True]
  else: # red
    tops.reverse()
    info.pop(idx)
    if not len(board[x][y]):
      if tops[0][0] not in info and idx<tops[0][0]:
        heapq.heappush(keys,tops[0][0])
      info[tops[0][0]]=[x,y,tops[0][1],True]

  board[x][y]+=tops
  if len(board[x][y])>=4:
    endFlag=True

def reverseDir(idx,d):
  if d==1:
    info[idx][2]=2
    return 2
  elif d==2:
    info[idx][2]=1
    return 1
  elif d==3:
    info[idx][2]=4
    return 4
  else:
    info[idx][2]=3
    return 3

def blue(idx,x,y,d,tops):
  d=reverseDir(idx,d)
  tops[0][1]=d
  if d==1: # right
    if y+1<N:
      if l[x][y+1]!=2:
        WhiteRedChange(idx,x,y+1,d,tops)
        return
  elif d==2: # left
    if y-1>=0:
      if l[x][y-1]!=2:
        WhiteRedChange(idx,x,y-1,d,tops)
        return
  elif d==3: # top
    if x-1>=0:
      if l[x-1][y]!=2:
        WhiteRedChange(idx,x-1,y,d,tops)
        return
  else: # bottom
    if x+1<N:
      if l[x+1][y]!=2:
        WhiteRedChange(idx,x+1,y,d,tops)
        return
  board[x][y]+=tops

def dirCheck(idx):
  [x,y,d,flag]=info[idx]
  tops=list(list(arr for arr in board[x][y]))
  board[x][y]=[]

  if d==1: # right
    if y+1<N:
      if l[x][y+1]!=2:
        WhiteRedChange(idx,x,y+1,d,tops)
        return
  elif d==2: # left
    if y-1>=0:
      if l[x][y-1]!=2:
        WhiteRedChange(idx,x,y-1,d,tops)
        return
  elif d==3: # top
    if x-1>=0:
      if l[x-1][y]!=2:
        WhiteRedChange(idx,x-1,y,d,tops)
        return
  else: # bottom
    if x+1<N:
      if l[x+1][y]!=2:
        WhiteRedChange(idx,x+1,y,d,tops)
        return
  blue(idx,x,y,d,tops) # 이동 불가능 or blue board

endFlag=False
time=0
while time<1000:
  time+=1
  keys=list(info.keys())
  heapq.heapify(keys)
  while keys:
    idx=heapq.heappop(keys)
    if idx in info and info[idx][3]:
      dirCheck(idx)

      # if time<=4:
      #   print('\n',time)
      #   print('changing...',idx)
      #   print(info)
      #   for item in board:
      #     print(item)

      if endFlag:
        print(time)
        exit(0)

print(-1)