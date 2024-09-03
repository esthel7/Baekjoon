import sys
input=sys.stdin.readline

N=int(input())
l=list(map(int,input().split()))

dp=[[False for i in range(N)]for j in range(N)]
for start in range(N):
  left=start
  for end in range(N-1,start-1,-1):
    if dp[start][end]:
      continue
    left=start
    right=end
    while left<=right:
      if l[left]==l[right]:
        left+=1
        right-=1
      else:
        break
    if left>=right:
      dp[start][end]=True
      left=start+1
      right=end-1
      while left<=right:
        dp[left][right]=True
        left+=1
        right-=1

M=int(input())
for i in range(M):
  a,b=map(int,input().split())
  if dp[a-1][b-1]:
    print(1)
  else:
    print(0)
