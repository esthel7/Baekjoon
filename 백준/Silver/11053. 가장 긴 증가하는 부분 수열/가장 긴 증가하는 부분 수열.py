import sys
input=sys.stdin.readline

N=int(input())
l=list(map(int,input().split()))

dp=[1 for i in range(N)]
# 1 2 1 3 2 4

# 10 20 30 5 6 7 8
for i in range(N):
  for j in range(i+1,N):
    if l[i]<l[j]:
      dp[j]=max(dp[j],dp[i]+1)

print(max(dp))
