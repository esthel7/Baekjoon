import sys
import heapq
input=sys.stdin.readline

V,E=map(int,input().split())

edges=[]
for i in range(E):
  a,b,w=map(int,input().split())
  if a<b:
    edges.append([w,a,b])
  elif a>b:
    edges.append([w,b,a])

answer=0
root=[20000 for i in range(V+1)]
info={} # save root info
heapq.heapify(edges)

while edges:
  [w,a,b]=heapq.heappop(edges)
  answer+=w
  if root[a]==root[b]:
    if root[a]!=20000:
      answer-=w
      continue
    else:
      info[a]=[a,b]
      root[a]=a
      root[b]=a
  else:
    if root[a]<root[b]:
      change=root[b]
      save=root[a]
      if root[b]==20000:
        info[save].append(b)
        root[b]=root[a]
        change=-1
    else:
      change=root[a]
      save=root[b]
      if root[a]==20000:
        info[save].append(a)
        root[a]=root[b]
        change=-1

    if change!=-1:
      for node in info[change]:
        info[save].append(node)
        root[node]=save
      info[change]=[]

print(answer)
