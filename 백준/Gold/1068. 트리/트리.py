import sys
input=sys.stdin.readline

N=int(input())

parent={}
children={}
for i in range(N):
  children[i]={}
  parent[i]=-1

l=list(map(int,input().split()))

for i in range(N):
  if l[i]!=-1:
    children[l[i]][i]=True
  parent[i]=l[i]

D=int(input())

q=[D]
while q:
  d=q.pop()
  if d in children:
    for child in children[d]:
      q.append(child)
    children.pop(d)
    p=parent[d]
    if p in children:
      children[p].pop(d)

cnt=0
for key in children:
  if not len(children[key]):
    cnt+=1

print(cnt)
