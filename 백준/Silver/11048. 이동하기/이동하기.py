import sys
input=sys.stdin.readline

N,M=map(int,input().split())
l=[]
for i in range(N):
  l.append(list(map(int,input().split())))

dp=[[[0 for i in range(3)]for j in range(M)]for k in range(N)]
xbox=[1,0,1]
ybox=[0,1,1]
dp[0][0]=[l[0][0],l[0][0],l[0][0]]
for i in range(N):
  for j in range(M):
    Max=max(dp[i][j])
    for k in range(3):
      if 0<=i+xbox[k]<N and 0<=j+ybox[k]<M:
        dp[i+xbox[k]][j+ybox[k]][k]=max(dp[i+xbox[k]][j+ybox[k]][k],Max+l[i+xbox[k]][j+ybox[k]])

print(max(dp[N-1][M-1]))
