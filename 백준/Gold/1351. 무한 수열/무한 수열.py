import sys
input=sys.stdin.readline

def find(N,P,Q):
  if N in dp:
    return dp[N]
  dp[N]=find(N//P,P,Q)+find(N//Q,P,Q)
  return dp[N]

N,P,Q=map(int,input().split())
if N==0:
  print(1)
  exit(0)

dp={}
dp[0]=1

find(N,P,Q)
print(dp[N])
