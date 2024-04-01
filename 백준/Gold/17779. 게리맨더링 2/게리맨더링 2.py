import sys
input=sys.stdin.readline

# 구역을 5개로 나누고 각 구역은 5개 선거구 중 하나에 포함
# 한 선거구에 포함되어있는 구역은 모두 연결되어야 함
# A에서 B가 연결될 때는 같은 구역

def calculate(x,y,d1,d2):
  l=list(list(arr) for arr in first)
  # 오른쪽위 사선
  j=y+1
  for i in range(x+1): # left part
    for k in range(j,N):
      total[1]+=l[i][k]
      l[i][k]=-2
  for i in range(x+1,x+d2+1): # 5 part
    total[4]+=l[i][j]
    l[i][j]=-5
    j+=1
    for k in range(j,N): # link part
      total[1]+=l[i][k]
      l[i][k]=-2

  # 오른쪽아래 사선
  j=y+d2-1
  for i in range(x+d2+1,x+d1+d2+1): # 5 part
    total[4]+=l[i][j]
    l[i][j]=-5
    for k in range(j+1,N): # link part
      total[3]+=l[i][k]
      l[i][k]=-4
    j-=1
  j=y-d1+d2
  for i in range(x+d1+d2+1,N): # left part
    for k in range(j,N):
      total[3]+=l[i][k]
      l[i][k]=-4

  # 왼쪽위 사선
  j=y
  for i in range(x): # left part
    for k in range(j+1):
      total[0]+=l[i][k]
      l[i][k]=-1
  for i in range(x,x+d1): # 5 part
    total[4]+=l[i][j]
    l[i][j]=-5
    if i!=x:
      for k in range(j+1,N): # mid part
        if l[i][k]==-5:
          break
        total[4]+=l[i][k]
        l[i][k]=-5
    for k in range(j): # link part
      total[0]+=l[i][k]
      l[i][k]=-1
    j-=1

  # 왼쪽아래 사선
  j=y-d1
  for i in range(x+d1,x+d1+d2): # 5 part
    total[4]+=l[i][j]
    l[i][j]=-5
    for k in range(j+1,N): # mid part
      if l[i][k]==-5:
        break
      total[4]+=l[i][k]
      l[i][k]=-5
    for k in range(j): # link part
      total[2]+=l[i][k]
      l[i][k]=-3
    j+=1
  j=y-d1+d2
  for i in range(x+d1+d2,N): # left part
    for k in range(j):
      total[2]+=l[i][k]
      l[i][k]=-3

N=int(input())
first=[]
for i in range(N):
  first.append(list(map(int,input().split())))

answer=-1
for x in range(N):
  for y in range(N):
    for d1 in range(1,N):
      for d2 in range(1,N):
        total=[0 for i in range(5)]
        if x+d1+d2<N and y-d1>=0 and y+d2<N:
          calculate(x,y,d1,d2)
          Min=min(total)
          Max=max(total)
          if answer==-1 or answer>Max-Min:
            answer=Max-Min

print(answer)
