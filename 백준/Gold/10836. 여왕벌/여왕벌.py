import sys
input=sys.stdin.readline

# 가장 왼쪽, 위쪽은 정해져있음
# 왼쪽, 대각선위, 위쪽 속도 중 가장 큰 속도만큼 자람

M,N=map(int,input().split())
bee=[[1 for i in range(M)]for j in range(M)]

for _ in range(N):
  items=list(map(int,input().split()))

  value=2
  for i in range(M):
    while items[-1]==0:
      items.pop()
      value-=1
      continue
    bee[0][M-1-i]+=value
    items[-1]-=1

  for i in range(1,M):
    while items[-1]==0:
      items.pop()
      value-=1
      continue
    bee[i][0]+=value
    items[-1]-=1

for i in range(M):
  print(bee[i][0],end=' ')
  for j in range(1,M):
    print(bee[0][j],end=' ')
  print()
