import sys
input=sys.stdin.readline

N=int(input())
if N==1:
  print(1)
  exit()
elif N==2:
  print(3)
  exit()

dp=[0 for i in range(N+1)] # 모든 경우의 수
dp[1]=1
dp[2]=2
for i in range(N-1):
  dp[i+2]+=dp[i]*2
  dp[i+1]+=dp[i]
dp[N]+=dp[N-1]

same=[0 for i in range(N+1)] # 대칭 경우의 수
same[1]=1
same[2]=3
for i in range(3,N+1):
  if i%2==0:
    same[i]=dp[i//2]+dp[i//2-1]*2
  else:
    same[i]=dp[(i-1)//2]

print(same[N]+(dp[N]-same[N])//2)
