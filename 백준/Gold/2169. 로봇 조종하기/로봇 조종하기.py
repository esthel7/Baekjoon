import sys
input=sys.stdin.readline

N,M=map(int,input().split())
l=[]
for i in range(N):
  l.append(list(map(int,input().split())))

visit=[[0 for i in range(M)]for j in range(N)]
visit[0][0]=l[0][0]

for i in range(1,M):
  visit[0][i]=visit[0][i-1]+l[0][i]

for i in range(1,N):
  first=[0 for j in range(M)]
  left=[0 for j in range(M)]
  right=[0 for j in range(M)]
  for j in range(M):
    first[j]=visit[i-1][j]+l[i][j]

  left[0]=first[0]
  for j in range(1,M):
    left[j]=max(first[j],left[j-1]+l[i][j])

  right[M-1]=first[M-1]
  visit[i][M-1]=max(right[M-1],left[M-1])
  for j in range(M-2,-1,-1):
    right[j]=max(first[j],right[j+1]+l[i][j])
    visit[i][j]=max(right[j],left[j])

print(visit[N-1][M-1])
