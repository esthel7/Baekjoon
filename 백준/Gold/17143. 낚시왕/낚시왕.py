import sys
import copy
input=sys.stdin.readline

# 사람이 y축 한칸 이동
# 해당 열 중 가장 위 상어 잡기
# 상어 이동 (벽에 부딪히면 방향 바꿔서 이동)
# 같은 칸에 여러 마리 있으면 크기 큰 상어만 남음

# 위, 아래, 오른쪽, 왼쪽

def saveTop(x,y):
  if y in newTop:
    if newTop[y]>x:
      newTop[y]=x
  else:
    newTop[y]=x


def save(x,y,size,dir,rate):
  if x in newShark:
    if y in newShark[x]:
      if newShark[x][y][0]>size:
        return
      newShark[x][y]=[size,dir,rate]
    else:
      newShark[x][y]=[size,dir,rate]
      saveTop(x,y)
  else:
    newShark[x]={y:[size,dir,rate]}
    saveTop(x,y)


R,C,M=map(int,input().split())

shark={} # 상어 위치 저장
top={} # 각 열마다 가장 위의 상어 x위치 저장

for i in range(M):
  r,c,s,d,z=map(int,input().split())
  r-=1
  c-=1
  if r in shark:
    shark[r][c]=[z,d,s] # 크기, 방향, 속력
  else:
    shark[r]={c:[z,d,s]}

  if c in top:
    if top[c]>r:
      top[c]=r
  else:
    top[c]=r

answer=0
person=0
while person<C and shark:
  if person in top:
    answer+=shark[top[person]][person][0]
    shark[top[person]].pop(person)

  newShark={}
  newTop={}
  for nowx in shark:
    for nowy in shark[nowx]:
      x=nowx
      y=nowy
      size,dir,rate=shark[x][y]

      nowrate=rate
      if nowrate==0:
        save(x,y,size,dir,rate)
      else:
        if dir in [1,2] and nowrate>=R+R-2:
          nowrate%=(R+R-2)
          if nowrate==0:
            if x==0 and dir==2:
              dir=1
            elif x==R-1 and dir==1:
              dir=2
            save(x,y,size,dir,rate)
        elif dir in [3,4] and nowrate>=C+C-2:
          nowrate%=(C+C-2)
          if nowrate==0:
            if y==0 and dir==3:
              dir=4
            elif y==C-1 and dir==4:
              dir=3
            save(x,y,size,dir,rate)

      while nowrate!=0:
        if dir==1: # top
          if x-nowrate>=0:
            save(x-nowrate,y,size,dir,rate)
            nowrate=0
          else:
            dir=2
            nowrate-=x
            x=0
        elif dir==2: # bottom
          if x+nowrate<R:
            save(x+nowrate,y,size,dir,rate)
            nowrate=0
          else:
            dir=1
            nowrate-=(R-x-1)
            x=R-1
        elif dir==3: # right
          if y+nowrate<C:
            save(x,y+nowrate,size,dir,rate)
            nowrate=0
          else:
            dir=4
            nowrate-=(C-y-1)
            y=C-1
        else: # left
          if y-nowrate>=0:
            save(x,y-nowrate,size,dir,rate)
            nowrate=0
          else:
            dir=3
            nowrate-=y
            y=0

  shark=copy.deepcopy(newShark)
  top=copy.deepcopy(newTop)
  person+=1

print(answer)

# 1 5 7 11 13 17 19 23
# 1 7 13 19
# 5 11 17 23


# 1 7 13
# 3 9 15

# 5 11
# 11
