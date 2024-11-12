import sys
from collections import deque
input=sys.stdin.readline

N=int(input())
l=list(map(int,input().split()))

dp=[-1 for i in range(N)]
dp[0]=0

q=deque([0])
while q:
  idx=q.popleft()
  if idx==N-1:
    print(dp[idx])
    exit()
  if l[idx]==0:
    continue
  for i in range(idx+1,idx+l[idx]+1):
    if i>=N:
      break
    if dp[i]==-1:
      dp[i]=dp[idx]+1
      q.append(i)

print(-1)
