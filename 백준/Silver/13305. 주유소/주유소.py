import sys
input=sys.stdin.readline

N=int(input())
dis=list(map(int,input().split()))
price=list(map(int,input().split()))

dp=[-1 for i in range(N)]
dp[0]=0

for i in range(N): 
  distance=0
  for j in range(i+1,N):
    distance+=dis[j-1]
    value=dp[i]+price[i]*distance
    if dp[j]==-1:
      dp[j]=value
    elif dp[j]<=value:
      break
    else:
      dp[j]=value

print(dp[N-1])
