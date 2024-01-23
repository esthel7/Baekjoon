import sys
input=sys.stdin.readline

def changeMaps(x,y):
  bottom=4
  if maps[x][y]==0:
    maps[x][y]=num[bottom]
  else:
    num[bottom]=maps[x][y]
    maps[x][y]=0

def exchange(a,b):
  tmp=num[a]
  num[a]=num[b]
  num[b]=tmp

def roll(dir):
  if dir==1: # 오른쪽
    exchange(0,1)
    exchange(0,2)
    exchange(0,4)
  elif dir==2: # 왼쪽
    exchange(1,0)
    exchange(1,2)
    exchange(2,4)
  elif dir==3: # 위
    exchange(1,5)
    exchange(1,3)
    exchange(3,4)
  else: # 아래
    exchange(1,3)
    exchange(1,4)
    exchange(1,5)

N,M,x,y,K=map(int,input().split())
num=[0,0,0,0,0,0] # 주사위
maps=[]
for i in range(N):
  maps.append(list(map(int,input().split())))
l=list(map(int,input().split()))

# x,y에 주사위 놓여있고, 모든 면에 0 적혀있음
# 주사위 굴렸을 때 이동칸에 적힌 수가 0이면 주사위 바닥 수가 칸에 복사
# 주사위 굴렸을 때 이동칸에 적힌 수가 0이 아니면 주사위 바닥 수가 바뀌고, 칸은 0이 됨
# 주사위는 지도 바깥으로 이동 불가, 출력 금지

now=[x,y]
top=1
changeMaps(x,y)

for i in range(K):
  if l[i]==1: # 오른쪽
    if now[1]+1>=M:
      continue
    now[1]+=1
  elif l[i]==2: # 왼쪽
    if now[1]-1<0:
      continue
    now[1]-=1
  elif l[i]==3: # 위
    if now[0]-1<0:
      continue
    now[0]-=1
  else: # 아래
    if now[0]+1>=N:
      continue
    now[0]+=1

  roll(l[i])
  changeMaps(now[0],now[1])
  print(num[top])
