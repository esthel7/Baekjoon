import sys
input=sys.stdin.readline

N=int(input())
l=[[]]
for i in range(N):
    a=[0]
    a+=(map(int,input().split()))
    l.append(a)

dp=[[[0 for i in range(N+1)]for i in range(N+1)]for i in range(3)]
# 처음은 0 가로, 1 세로, 2 대각선 구분 위함

dp[0][1][2]=1 # 가로이며, (1,2)에 파이프 있음

for i in range(1,N+1):
    for j in range(1,N+1):
        if l[i][j]!=0:
            continue

        # 가로
        dp[0][i][j]+=dp[0][i][j-1] # 옆
        if i-1>=1 and l[i-1][j]==0 and j-1>=1 and l[i][j-1]==0: # 대각선
            dp[2][i][j]+=dp[0][i-1][j-1]

        # 세로
        dp[1][i][j]+=dp[1][i-1][j] # 아래
        if i-1>=1 and l[i-1][j]==0 and j-1>=1 and l[i][j-1]==0: # 대각선
            dp[2][i][j]+=dp[1][i-1][j-1]

        # 대각선
        dp[0][i][j]+=dp[2][i][j-1] # 옆
        dp[1][i][j]+=dp[2][i-1][j] # 아래
        if i-1>=1 and l[i-1][j]==0 and j-1>=1 and l[i][j-1]==0: # 대각선
            dp[2][i][j]+=dp[2][i-1][j-1]

print(dp[0][N][N]+dp[1][N][N]+dp[2][N][N])
