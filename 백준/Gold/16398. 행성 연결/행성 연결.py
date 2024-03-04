import sys
input=sys.stdin.readline

N=int(input())
l=[]

for i in range(N):
  l.append(list(map(int,input().split())))

edges=[]
for i in range(N):
  for j in range(i+1,N):
    edges.append([l[i][j],i,j])

edges.sort(reverse=True)

root=[2000 for i in range(N)]
info={}
answer=0
while edges:
  [w,a,b]=edges.pop()
  answer+=w
  if root[a]==root[b]:
    if root[a]!=2000:
      answer-=w
      continue
    root[a]=a
    root[b]=a
    info[a]=[a,b]
  else:
    if root[a]>root[b]:
      change=root[a]
      save=root[b]
      if root[a]==2000:
        root[a]=save
        info[save].append(a)
        change=-1
    else:
      change=root[b]
      save=root[a]
      if root[b]==2000:
        root[b]=save
        info[save].append(b)
        change=-1

    if change!=-1:
      for node in info[change]:
        root[node]=save
        info[save].append(node)
      info[change]=[]

print(answer)

