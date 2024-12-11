import sys
input=sys.stdin.readline

def find(node,cnt):
  if cnt==5:
    print(1)
    exit()
  for link in graph[node].keys():
    if not visited[link]:
      visited[link]=True
      find(link,cnt+1)
      visited[link]=False


N,M=map(int,input().split())
graph={}
for i in range(M):
  a,b=map(int,input().split())
  if a in graph:
    graph[a][b]=True
  else:
    graph[a]={b:True}
  if b in graph:
    graph[b][a]=True
  else:
    graph[b]={a:True}

for i in range(N):
  if i not in graph:
    continue
  visited=[False for i in range(N)]
  visited[i]=True
  find(i,1)

print(0)

