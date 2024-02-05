import sys
input=sys.stdin.readline

n=int(input())
l=[]
dp=[]
for i in range(n):
  l.append(list(map(int,input().split())))
  dp.append([-1 for j in range(i+1)])

dp[0][0]=l[0][0]
for i in range(1,n):
  for j in range(i+1):
    if j-1>=0 and dp[i][j]<dp[i-1][j-1]+l[i][j]:
      dp[i][j]=dp[i-1][j-1]+l[i][j]
    if j<i and dp[i][j]<dp[i-1][j]+l[i][j]:
      dp[i][j]=dp[i-1][j]+l[i][j]

print(max(dp[n-1]))
