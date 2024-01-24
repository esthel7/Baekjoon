import sys
input=sys.stdin.readline

def find(N,M,A,B):
  A.sort()
  B.sort()
  now=0
  last=0
  for i in range(N):
    for j in range(last,M):
      if A[i]<=B[j]:
        last=j
        break
      if j==M-1:
        last=j+1
    now+=last
  print(now)

T=int(input())
for i in range(T):
  N,M=map(int,input().split())
  A=list(map(int,input().split()))
  B=list(map(int,input().split()))
  find(N,M,A,B)
