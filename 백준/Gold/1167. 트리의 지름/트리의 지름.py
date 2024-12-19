import sys
input=sys.stdin.readline

V=int(input())
graph={}
for i in range(V):
  now=list(map(int,input().split()))
  graph[now[0]]={now[0]:0}
  for j in range(1,len(now)-1,2):
    graph[now[0]][now[j]]=now[j+1]


def find(root):
  q=[]
  visited=[-1 for i in range(V+1)]
  far=[0,0]
  for key in graph[root].keys():
    visited[key]=graph[root][key]
    q.append(key)

  while q:
    node=q.pop()
    if far[0]<visited[node]:
      far=[visited[node],node]
    for key in graph[node].keys():
      if visited[key]==-1:
        visited[key]=graph[node][key]+visited[node]
        q.append(key)
  return far


far=find(1)
answer=find(far[1])

print(answer[0])
