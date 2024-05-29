import sys
input=sys.stdin.readline

N=int(input())
dp=[0 for i in range(N+2)]
for i in range(N+1):
  if i==0:
    continue
  t,p=map(int,input().split())
  dp[i]=max(dp[i-1],dp[i])
  if i+t<=N+1:
    dp[i+t]=max(dp[i+t],dp[i]+p)

dp[N+1]=max(dp[N],dp[N+1])
print(dp[N+1])
