import sys
input=sys.stdin.readline

N=int(input())
l=[]
for i in range(N):
  l.append(list(map(int,input().split())))
l.sort()

dp=[0 for i in range(N)]
for i in range(N):
  now=l[i][1]
  for j in range(i+1,N):
    if now<l[j][1]:
      dp[j]=max(dp[j],dp[i]+1)

print(N-max(dp)-1)
