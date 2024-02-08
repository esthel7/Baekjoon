import sys
input=sys.stdin.readline

def find(N,M):
  dp=[0 for j in range(M+1)]
  dp[0]=1
  for i in range(N):
    for j in range(l[i],M+1):
      dp[j]+=dp[j-l[i]]

  print(dp[M])

T=int(input())
for i in range(T):
  N=int(input())
  l=list(map(int,input().split()))
  M=int(input())
  find(N,M)
