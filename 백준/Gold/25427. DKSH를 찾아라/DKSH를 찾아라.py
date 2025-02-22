import sys
input=sys.stdin.readline

N=int(input())
S=list(input().rstrip())

dp=[0 for i in range(4)]
for i in range(N):
  if S[i]=='D':
    dp[0]+=1
  elif S[i]=='K':
    dp[1]+=dp[0]
  elif S[i]=='S':
    dp[2]+=dp[1]
  elif S[i]=='H':
    dp[3]+=dp[2]

print(dp[3])
