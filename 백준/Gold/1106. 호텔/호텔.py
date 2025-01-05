import sys
input=sys.stdin.readline

C,N=map(int,input().split())
dp=[0 for i in range(C+1)]
for i in range(N):
  cost,num=map(int,input().split())
  if num>=C:
    if dp[C]==0 or dp[C]>cost:
      dp[C]=cost
    continue
  for j in range(num+1):
    if dp[j]==0 or dp[j]>cost:
      dp[j]=cost
  for j in range(num+1,C+1):
    if dp[j]==0 or dp[j]>dp[j-num]+cost:
      dp[j]=dp[j-num]+cost

print(dp[C])
