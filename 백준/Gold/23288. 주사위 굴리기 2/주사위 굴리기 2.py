import sys
input=sys.stdin.readline

# 이동 방향으로 한 칸 굴러감, 벽이라면 반대로 한칸 굴러감
# 도착 칸에 대한 점수 획득

# 아랫면과 지도칸 비교해 이동방향 결정
# 아랫면이 크면 90도 시계방향 회전
# 지도칸이 크면 90도 반시계방향 회전
# 같다면 이동방향 변경 x

# 점수는 동서남북 방향으로 연속해서 이동할 수 있는 칸(B가 쓰여있어야함)의 수 C * 지도칸 B

def changeTop():
  global box
  box=[box[1],box[2],box[3],box[0],box[4],box[5]]

def changeBottom():
  global box
  box=[box[3],box[0],box[1],box[2],box[4],box[5]]

def changeLeft():
  global box
  # 4 1 3
  #   5
  #   6
  #   2

  # 1 3 6
  #   5
  #   4
  #   2
  box=[box[5],box[1],box[4],box[3],box[0],box[2]]

def changeRight():
  global box
  # 4 1 3
  #   5
  #   6
  #   2

  # 6 4 1
  #   5
  #   3
  #   2
  box=[box[4],box[1],box[5],box[3],box[2],box[0]]


Top=0
Right=1
Bottom=2
Left=3

N,M,K=map(int,input().split())
l=[]
for i in range(N):
  l.append(list(map(int,input().split())))

box=[1,5,6,2,4,3]
dir=Right
now=[0,0]
answer=0
xbox=[-1,1,0,0]
ybox=[0,0,-1,1]

for _ in range(K):
  while True:
    if dir==Top:
      if now[0]-1<0:
        dir=Bottom
        continue
      changeTop()
      now[0]-=1
      break
    elif dir==Bottom:
      if now[0]+1>=N:
        dir=Top
        continue
      changeBottom()
      now[0]+=1
      break
    elif dir==Left:
      if now[1]-1<0:
        dir=Right
        continue
      changeLeft()
      now[1]-=1
      break
    else: # Right
      if now[1]+1>=M:
        dir=Left
        continue
      changeRight()
      now[1]+=1
      break

  # 점수 계산
  map=l[now[0]][now[1]]
  visited=[[False for i in range(M)]for j in range(N)]
  visited[now[0]][now[1]]=True
  q=[[now[0],now[1]]]
  cnt=0
  while q:
    x,y=q.pop()
    cnt+=1
    for i in range(4):
      newX=x+xbox[i]
      newY=y+ybox[i]
      if 0<=newX<N and 0<=newY<M and not visited[newX][newY] and l[newX][newY]==map:
        visited[newX][newY]=True
        q.append([newX,newY])
  answer+=map*cnt

  bottom=box[2]
  if bottom>map:
    dir+=1
    dir%=4
  elif bottom<map:
    dir+=3
    dir%=4

print(answer)
