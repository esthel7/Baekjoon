import sys
input=sys.stdin.readline

# 가장 왼쪽, 위쪽은 정해져있음
# 왼쪽, 대각선위, 위쪽 속도 중 가장 큰 속도만큼 자람

M,N=map(int,input().split())
bee=[[1 for i in range(M)]for j in range(M)]

for _ in range(N):
  items=list(map(int,input().split()))
  grow=[]
  for idx in range(3):
    for item in range(items[idx]):
      grow.append(idx)

  now=[[0 for i in range(M)]for j in range(M)]
  for i in range(M):
    now[M-1-i][0]=grow[i]
    bee[M-1-i][0]+=grow[i]
  for i in range(M,len(grow)):
    now[0][i+1-M]=grow[i]
    bee[0][i+1-M]+=grow[i]

  for i in range(1,M):
    for j in range(1,M):
      value=max(now[i-1][j-1],now[i-1][j],now[i][j-1])
      now[i][j]=value
      bee[i][j]+=now[i][j]

for i in range(M):
  for j in range(M):
    print(bee[i][j],end=' ')
  print()
