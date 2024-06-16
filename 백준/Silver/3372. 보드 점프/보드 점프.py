import sys
input=sys.stdin.readline

N=int(input())
l=[]
for i in range(N):
  l.append(list(map(int,input().split())))

visit=[[0 for i in range(N)]for j in range(N)]
visit[0][0]=1
for i in range(N):
  for j in range(N):
    if i==N-1 and j==N-1:
      break
    if visit[i][j]!=0:
      cnt=l[i][j]
      if i+cnt<N:
        visit[i+cnt][j]+=visit[i][j]
      if j+cnt<N:
        visit[i][j+cnt]+=visit[i][j]

print(visit[N-1][N-1])
