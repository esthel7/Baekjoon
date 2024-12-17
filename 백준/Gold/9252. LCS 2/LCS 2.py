import sys
input=sys.stdin.readline

A=['']+list(input().rstrip())
B=['']+list(input().rstrip())

dp=[['' for i in range(len(B))]for j in range(len(A))]

for i in range(1,len(A)):
  for j in range(1,len(B)):
    if A[i]==B[j]:
      dp[i][j]=dp[i-1][j-1]+A[i]
    else:
      if len(dp[i-1][j])>len(dp[i][j-1]):
        dp[i][j]=dp[i-1][j]
      else:
        dp[i][j]=dp[i][j-1]

print(len(dp[-1][-1]))
print(dp[-1][-1])
# A C A Y K P
# C A P C A K

# 1 0 5 1 0 4
#   2     2

# [[1], [0, 2], [5], [1], [0, 2], [4]]

