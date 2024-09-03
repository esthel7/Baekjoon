import sys
input=sys.stdin.readline

a=list(input().rstrip())
b=list(input().rstrip())

A=len(a)
B=len(b)

answer=0
dp=[[0 for i in range(B)]for j in range(A)]
for i in range(A):
  for j in range(B):
    if a[i]==b[j]:
      if i!=0 and j!=0:
        dp[i][j]+=dp[i-1][j-1]+1
        answer=max(answer,dp[i][j])
      else:
        dp[i][j]=1

print(answer)
