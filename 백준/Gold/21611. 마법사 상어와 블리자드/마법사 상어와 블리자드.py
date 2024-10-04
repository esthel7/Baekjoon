import sys
input=sys.stdin.readline

# 상어 위치 제외하고 구슬 1,2,3번이 들어감

# 상어는 특정 방향으로 특정 거리만큼 모든 칸의 구슬 파괴 -> 빈칸이 됨
# 번호가 하나 작은 칸이 빈칸이 되면 구슬이 그 칸으로 이동, 더이상 이동 없을때까지 반복

# 4개이상 연속(벽 통과 x)하는 구슬 있으면 폭발 
# 폭발 후에도 번호 하나 작은 칸이 빈칸되면 구슬이 그 칸으로 이동, 더이상 이동 없을때까지 반복
# 연속 구슬 있으면 폭발, 채우기 ... 반복

# 연속되는 구슬의 개수와 번호로 변경, 칸 수보다 많아지면 스탑

def fillNumAndMakeLine():
  xbox=[0,1,0,-1]
  ybox=[-1,0,1,0]
  x=N//2
  y=N//2
  number=1
  cnt=2
  while True:
    for i in range(2):
      for _ in range(cnt//2):
        x+=xbox[i]
        y+=ybox[i]
        num[x][y]=number
        line.append(l[x][y])
        number+=1
        if number==Last:
          return
    cnt+=2
    for i in range(2,4):
      for _ in range(cnt//2):
        x+=xbox[i]
        y+=ybox[i]
        num[x][y]=number
        line.append(l[x][y])
        number+=1
        if number==Last:
          return
    cnt+=2


def moveBall(empty):
  global line
  while empty:
    idx=empty.pop()
    line=line[:idx]+line[idx+1:]
    line.append(0)


def popBall(empty):
  global line
  while empty:
    start,cnt=empty.pop()
    bomb[line[start]]+=cnt
    line=line[:start]+line[start+cnt:]


def shark(d,s):
  x=N//2
  y=N//2
  empty=[]
  if d==Top:
    for i in range(1,s+1):
      # bomb[line[num[x-i][y]]]+=1
      empty.append(num[x-i][y])
  elif d==Bottom:
    for i in range(1,s+1):
      # bomb[line[num[x+i][y]]]+=1
      empty.append(num[x+i][y])
  elif d==Left:
    for i in range(1,s+1):
      # bomb[line[num[x][y-i]]]+=1
      empty.append(num[x][y-i])
  else:
    for i in range(1,s+1):
      # bomb[line[num[x][y+i]]]+=1
      empty.append(num[x][y+i])
  moveBall(empty)


def changeBoard():
  global line
  start=0
  cnt=0
  s=[]
  Line=len(line)
  for i in range(1,Line):
    if line[i]==0 or i==Line-1:
      s.append([cnt,line[start]])
      break
    if line[start]==line[i]:
      cnt+=1
    else:
      if cnt!=0:
        s.append([cnt,line[start]])
      cnt=1
      start=i
  now=1
  line=[0]
  for cnt,number in s:
    line.append(cnt)
    now+=1
    if now==Last:
      break
    line.append(number)
    now+=1
    if now==Last:
      break
  for i in range(now,Last):
    line.append(0)


def find():
  flag=True
  while flag:
    empty=[]
    flag=False
    start=0
    cnt=0
    for i in range(1,Last):
      if line[i]==0 or i==Last-1:
        if cnt>=4:
          empty.append([start,cnt])
        popBall(empty)
        break
      if line[start]==line[i]:
        cnt+=1
      else:
        if cnt>=4:
          flag=True
          empty.append([start,cnt])
        cnt=1
        start=i
  changeBoard()


N,M=map(int,input().split())
l=[]
line=[0]
for i in range(N):
  now=list(map(int,input().split()))
  l.append(now)

Last=N*N
num=[[0 for i in range(N)]for j in range(N)] # 번호 매긴 판
fillNumAndMakeLine()

bomb=[0 for i in range(4)] # 터진 구슬 수
Top=1
Bottom=2
Left=3
Right=4
for i in range(M):
  d,s=map(int,input().split())
  shark(d,s)
  find()

print(1*bomb[1]+2*bomb[2]+3*bomb[3])
