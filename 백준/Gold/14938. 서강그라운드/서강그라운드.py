import sys
input=sys.stdin.readline

n,m,r=map(int,input().split())
item=[0]+list(map(int,input().split()))

graph=[[]for i in range(n+1)]
for _ in range(r):
  a,b,L=map(int,input().split())
  if L>m:
    continue
  graph[a].append([b,L]) # node, len
  graph[b].append([a,L])

answer=0
for i in range(1,n+1):
  visited=[-1 for i in range(n+1)]
  cnt=item[i]
  q=[[0,i]]
  visited[i]=0

  while q:
    [now,idx]=q.pop()
    for [node,L] in graph[idx]:
      if now+L<=m:
        if visited[node]==-1:
          visited[node]=now+L
          cnt+=item[node]
        elif visited[node]>now+L:
          visited[node]=now+L
        else:
          continue

        q.append([now+L,node])

  if answer<cnt:
    answer=cnt

print(answer)
