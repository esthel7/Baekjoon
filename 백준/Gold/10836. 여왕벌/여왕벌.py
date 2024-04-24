import sys
input=sys.stdin.readline

# 가장 왼쪽, 위쪽은 정해져있음
# 왼쪽, 대각선위, 위쪽 속도 중 가장 큰 속도만큼 자람

M,N=map(int,input().split())
side=[0 for i in range(2*M-1)]

for _ in range(N):
  items=list(map(int,input().split()))
  if items[0]<2*M-1:
    side[items[0]]+=1
  if items[0]+items[1]<2*M-1:
    side[items[0]+items[1]]+=1

for i in range(1,2*M-1):
  side[i]+=side[i-1]

for i in range(M-1,-1,-1):
  print(1+side[i],end=' ')
  for j in range(M,2*M-1):
    print(1+side[j],end=' ')
  print()
