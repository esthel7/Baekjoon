import sys
input=sys.stdin.readline

n=int(input())
l=[]
for i in range(n):
  l.append(int(input()))

dp=[[0,0,0] for i in range(n)]
dp[0][0]=l[0]
dp[0][1]=l[0]
if n>1:
  dp[1][0]=dp[0][0]+l[1]
  dp[1][1]=l[1]
  dp[1][2]=dp[0][0]
for i in range(2,n):
  pprev=max(dp[i-2])
  prev=max(dp[i-1])
  listprev=dp[i-1][1]
  dp[i][0]=listprev+l[i]
  dp[i][1]=pprev+l[i]
  dp[i][2]=prev

print(max(dp[n-1]))
