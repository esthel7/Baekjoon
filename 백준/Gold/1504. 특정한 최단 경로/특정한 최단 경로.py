import sys
import heapq
input=sys.stdin.readline

def find(start,line):
  q=[]
  for i in range(1,N+1):
    if graph[start][i]!=0:
      visited[line][i]=graph[start][i]
      heapq.heappush(q,[graph[start][i],i])

  while q:
    cost,idx=heapq.heappop(q)
    if visited[line][idx]!=cost:
      continue
    for i in range(1,N+1):
      if graph[idx][i]!=0 and (visited[line][i]==0 or visited[line][i]>cost+graph[idx][i]):
        visited[line][i]=cost+graph[idx][i]
        heapq.heappush(q,[cost+graph[idx][i],i])


N,E=map(int,input().split())
graph=[[0 for i in range(N+1)]for j in range(N+1)]
for i in range(E):
  a,b,c=map(int,input().split())
  if a==b:
    continue
  graph[a][b]=c
  graph[b][a]=c
u,v=map(int,input().split())

visited=[[0 for i in range(N+1)]for j in range(3)]
find(1,0)
find(u,1)
find(v,2)

if (u==1 and v==N) or (u==N and v==1):
  if visited[0][N]!=0:
    print(visited[0][N])
  else:
    print(-1)
  exit()

answer=-1
if visited[0][u]!=0 and visited[1][v]!=0 and visited[2][N]!=0:
  answer=visited[0][u]+visited[1][v]+visited[2][N]

if visited[0][u]!=0 and visited[1][v]!=0 and visited[2][N]!=0 and (answer==-1 or answer>visited[0][v]+visited[2][u]+visited[1][N]):
  answer=visited[0][v]+visited[2][u]+visited[1][N]

print(answer)
