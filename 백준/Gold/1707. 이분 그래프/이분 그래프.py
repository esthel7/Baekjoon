import sys
input=sys.stdin.readline

K=int(input())
for _ in range(K):
  V,E=map(int,input().split())
  link={}
  for i in range(1,V+1):
    link[i]=[]

  for __ in range(E):
    u,v=map(int,input().split())
    link[u].append(v)
    link[v].append(u)


  def fill(key):
    global flag
    color[key]='R'
    q=[key]
    visited[key]=True
    while q:
      key=q.pop()
      now=color[key]
      if now=='R':
        fillColor='B'
      else:
        fillColor='R'
      for node in link[key]:
        if color[node]=='N':
          color[node]=fillColor
        elif color[node]!=fillColor:
          flag=True
          return
        if not visited[node]:
          visited[node]=True
          q.append(node)


  color=['N' for i in range(V+1)]
  visited=[False for i in range(V+1)]
  flag=False
  for i in range(1,V+1):
    if not visited[i]:
      fill(i)
      if flag:
        break

  if not flag:
    print('YES')
  else:
    print('NO')
