import sys
input=sys.stdin.readline

n=int(input())
if n==1:
  print(1)
  exit(0)

dp=[0 for i in range(n+1)]
dp[0]=1
dp[1]=1
for i in range(2,n+1):
  dp[i]=dp[i-2]*2+dp[i-1]

print(dp[n]%10007)
