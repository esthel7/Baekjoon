n=int(input())
l=list(map(int,input().split()))

dp=[-100000000 for i in range(n+1)]
dp[0]=l[0]
for i in range(1,n):
  now=max(dp[i-1]+l[i],l[i])
  dp[i]=now

print(max(dp))
