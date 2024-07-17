import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
  N,M=map(int,input().split())
  top=1
  for i in range(N):
    top*=M-i
  bottom=1
  for i in range(1,N+1):
    bottom*=i
  print(top//bottom)
