import sys
input=sys.stdin.readline

a=input().rstrip()
b=input().rstrip()

A=len(a)
B=len(b)

dp=[[0 for i in range(A)] for j in range(B)]
answer=0

for i in range(B):
  for j in range(A):
    if b[i]==a[j]:
      if i!=0 and j!=0:
        dp[i][j]=dp[i-1][j-1]+1
        if answer<dp[i][j]:
          answer=dp[i][j]
      else:
        dp[i][j]=1
        if answer==0:
          answer=1

print(answer)
