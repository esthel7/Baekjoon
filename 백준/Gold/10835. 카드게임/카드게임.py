import sys
input=sys.stdin.readline

N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

dp=[[-1 for i in range(N+1)]for j in range(N+1)]
dp[0][0]=0
answer=0
for i in range(N):
  for j in range(N):
    if dp[i][j]==-1:
      continue
    if A[i]>B[j] and dp[i][j+1]<dp[i][j]+B[j]:
      dp[i][j+1]=dp[i][j]+B[j]
      if answer<dp[i][j+1]:
        answer=dp[i][j+1]
    else:
      dp[i+1][j]=max(dp[i+1][j],dp[i][j])
      dp[i+1][j+1]=max(dp[i+1][j+1],dp[i][j])

print(answer)

# 왼쪽 혹은 왼오 버리기
# 오른쪽이 왼쪽보다 작으면 오른쪽 버리는데 적힌 수만큼 점수 얻음
# 한쪽이라도 사라지면 게임 끝
