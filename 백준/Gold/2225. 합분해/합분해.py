import sys
input=sys.stdin.readline


N,K=map(int,input().split())

final=[[1 for i in range(N+1)]for j in range(K)]
for i in range(1,K):
  for j in range(1,N+1):
    final[i][j]=final[i-1][j]+final[i][j-1]

print(final[K-1][N]%1000000000)
