import sys
input=sys.stdin.readline

N=int(input())

dp=[i for i in range(N+1)] # 다 한번씩만 눌렀을 경우
for i in range(7,N+1):
    dp[i]=max(dp[i-3]*2,dp[i-4]*3,dp[i-5]*4) # 복붙 횟수
print(dp[N])
