import sys
input=sys.stdin.readline

V,E=map(int,input().split())
q=[]
visited=[[-1 for i in range(V)]for j in range(V)]
for i in range(E):
  a,b,c=map(int,input().split())
  a-=1
  b-=1
  if visited[a][b]==-1 or visited[a][b]>c:
    visited[a][b]=c
  for j in range(V):
    if visited[j][a]!=-1:
      if visited[j][b]==-1 or visited[j][b]>visited[j][a]+c:
        visited[j][b]=visited[j][a]+c
  for j in range(V):
    if visited[b][j]!=-1:
      if visited[a][j]==-1 or visited[a][j]>visited[b][j]+c:
        visited[a][j]=visited[b][j]+c

# print(visited)
answer=-1
for i in range(V):
  if visited[i][i]!=-1 and (answer==-1 or answer>visited[i][i]):
    answer=visited[i][i]

print(answer)
