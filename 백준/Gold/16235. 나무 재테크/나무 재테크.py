import sys
from collections import deque
input=sys.stdin.readline

# 처음 양분은 모든 칸에 5만큼 들어있음
# 한 칸에 여러개 나무도 가능

# 나이만큼 양분 먹고 나이 1 증가, 각 나무는 칸의 양분만 먹을 수 있음
# 칸에 여러 나무가 있다면 나이 어린 나무부터 양분 먹음
# 양분이 부족해 나이만큼 양분을 못먹으면 즉시 죽음

# 죽은 나무는 나이의 절반이 양분으로 변함

# 나이가 5의 배수면 번식, 인접한 8개 칸에 나이가 1인 나무 생김
# 땅에 양분이 추가됨

N,M,K=map(int,input().split())
land=[[5 for i in range(N)]for j in range(N)]
plus=[] # 겨울에 추가되는 비료 저장
tree=[[deque([]) for i in range(N)]for j in range(N)]
cnt=M # 나무 개수

for i in range(N):
  plus.append(list(map(int,input().split())))

for i in range(M):
  x,y,age=map(int,input().split())
  x-=1
  y-=1
  tree[x][y].append(age)

xbox=[-1,1,0,0,-1,-1,1,1]
ybox=[0,0,-1,1,-1,1,-1,1]
time=0
while time<K:
  time+=1

  # spring
  die={}
  for x in range(N):
    for y in range(N):
      now=0 # 추가할 양분
      new=deque([]) # 성장한 나무
      while tree[x][y]:
        age=tree[x][y].popleft()
        if age<=land[x][y]:
          land[x][y]-=age
          new.append(age+1)
        else:
          cnt-=1
          now+=age//2

      if new:
        tree[x][y]=new
      if now:
        if x in die:
          die[x][y]=now
        else:
          die[x]={y:now}

  # summer
  for x in die:
    for y in die[x]:
      land[x][y]+=die[x][y]

  # fall
  for x in range(N):
    for y in range(N):
      for age in tree[x][y]:
        if age%5==0:
          for i in range(8):
            newX=x+xbox[i]
            newY=y+ybox[i]
            if 0<=newX<N and 0<=newY<N:
              tree[newX][newY].appendleft(1)
              cnt+=1

  # winter
  for x in range(N):
    for y in range(N):
      land[x][y]+=plus[x][y]

print(cnt)
