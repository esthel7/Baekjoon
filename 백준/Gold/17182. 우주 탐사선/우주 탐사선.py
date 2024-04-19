import sys
input=sys.stdin.readline

def find(node,cnt,visit):
  global answer
  if len(visit)==N:
    if answer==-1 or answer>cnt:
      answer=cnt
    return

  for i in range(N):
    if i==node or i in visit:
      continue
    newVisit=list(visit)
    newVisit.append(i)
    find(i,cnt+l[node][i],newVisit)

N,K=map(int,input().split())
l=[]
for i in range(N):
  l.append(list(map(int,input().split())))

for k in range(N):
  for i in range(N):
    for j in range(N):
      l[i][j] = min(l[i][j],l[i][k]+l[k][j])

answer=-1
find(K,0,[K])
print(answer)
