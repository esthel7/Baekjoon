import sys
input=sys.stdin.readline

# 1번은 강력해 나머지 모두 쫓아낼 수 있음
# 상하좌우로 한칸씩 이동, 존재하는 칸에 냄새 뿌림
# 냄새는 k번 이동하면 사라짐

# 아무 냄새 없는 칸으로 이동, 없다면 자신의 냄새칸으로 이동 -> 여러개라면 우선순위순

# 모든 상어가 이동한 훙 한 칸에 여러마리의 상어가 있다면 가장 작은 번호의 상어만 남음

N,M,K=map(int,input().split())

loc={} # 현재 상어 위치
l=[[[]for i in range(N)]for j in range(N)]  # 상어 냄새 보관
for i in range(N):
  board=list(map(int,input().split()))
  for j in range(N):
    if board[j]!=0:
      loc[board[j]]=[i,j]
      l[i][j]=[board[j],0] # num, time
    else:
      l[i][j]=[0,0]

dir=[0]+list(map(int,input().split())) # 현재 상어 방향

move=[[]for i in range(M+1)] # 상어별 우선순위
for i in range(1,M+1):
  move[i].append([])
  for j in range(4):
    move[i].append(list(map(int,input().split())))

# 위, 아래, 좌, 우
for time in range(1,1001):
  newL={}
  for num in loc:
    x=loc[num][0]
    y=loc[num][1]
    nowdir=dir[num]
    possible=[] # 이동 가능한 보드
    zeroflag=False
    for moving in move[num][nowdir]:
      newX=x
      newY=y
      if moving==1: # top
        newX=x-1
      elif moving==2: # bottom
        newX=x+1
      elif moving==3: # left
        newY=y-1
      else: # right
        newY=y+1

      if 0<=newX<N and 0<=newY<N:
        if l[newX][newY][0]!=0 and (l[newX][newY][0]!=num and l[newX][newY][1]>=time-K):
          continue
        if l[newX][newY][0]!=0 and l[newX][newY][1]<time-K:
          l[newX][newY][0]=0

        if l[newX][newY][0]==0:
          if newX in newL:
            if newY in newL[newX]:
              newL[newX][newY].append([num,moving])
            else:
              newL[newX][newY]=[[num,moving]]
          else:
            newL[newX]={newY:[[num,moving]]}
          zeroflag=True
          break
        elif l[newX][newY][0]==num:
          possible.append([newX,newY,moving])

    if not zeroflag: # 기존 칸으로 이동
      [newX,newY,moving]=possible[0]
      if newX in newL:
        if newY in newL[newX]:
          newL[newX][newY].append([num,moving])
        else:
          newL[newX][newY]=[[num,moving]]
      else:
        newL[newX]={newY:[[num,moving]]}

  for x in newL:
    for y in newL[x]:
      if len(newL[x][y])>=2:
        [num,moving]=min(newL[x][y])
        for [leftNum,leftMoving] in newL[x][y]:
          if leftNum==num:
            continue
          loc.pop(leftNum)
      else:
        [num,moving]=newL[x][y][0]

      l[x][y]=[num,time]
      loc[num]=[x,y]
      dir[num]=moving

  if len(loc)==1:
    print(time)
    exit(0)

print(-1)
