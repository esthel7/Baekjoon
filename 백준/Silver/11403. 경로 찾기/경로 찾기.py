import sys
input=sys.stdin.readline

N=int(input())
graph={}
for i in range(N):
  graph[i]={}

visited=[['0' for i in range(N)]for j in range(N)]
for i in range(N):
  now=list(map(int,input().split()))
  for j in range(N):
    if now[j]==1:
      graph[i][j]=True
      visited[i][j]='1'

for start in range(N):
  q=list(graph[start].keys())
  while q:
    end=q.pop()
    for key in graph[end]:
      if visited[start][key]=='1':
        continue
      visited[start][key]='1'
      q.append(key)

for i in range(N):
  print(' '.join(visited[i]))
