import sys
input=sys.stdin.readline

def find(n):
  dp=[[0 for i in range(n)]for i in range(5)]

  dp[0][0]=l[0][0]
  dp[1][0]=l[1][0]
  if n>=2:
    dp[0][1]=dp[1][0]+l[0][1]
    dp[1][1]=dp[0][0]+l[1][1]

  for i in range(2,n):
    dp[0][i]=l[0][i]+max(dp[1][i-1],dp[1][i-2])
    dp[1][i]=l[1][i]+max(dp[0][i-1],dp[0][i-2])

  print(max(dp[0][n-1],dp[1][n-1]))

T=int(input())
for i in range(T):
  n=int(input())
  l=[]
  l.append(list(map(int,input().split())))
  l.append(list(map(int,input().split())))
  find(n)
