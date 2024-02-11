import sys
input=sys.stdin.readline

n,m=map(int,input().split())
l=[]
for i in range(n):
  l.append(list(input().rstrip()))

answer=0
dp=[[0 for i in range(m)]for j in range(n)]
dp[0][0]=int(l[0][0])
if dp[0][0]>answer:
  answer=1

for i in range(1,m):
  dp[0][i]=int(l[0][i])
  if dp[0][i]>answer:
    answer=1

for i in range(1,n):
  dp[i][0]=int(l[i][0])
  if dp[i][0]>answer:
    answer=1

for i in range(1,n):
  for j in range(1,m):
    if l[i][j]=='0':
      dp[i][j]=0
    else:
      possible=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
      dp[i][j]=possible+1
      value=(possible+1)*(possible+1)
      if answer<value:
        answer=value

print(answer)
