import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(r):
  if len(children[r])==0:
    return 1
  for node in children[r]:
    if answers[node]==0:
      answers[node]=find(node)
    answers[r]+=answers[node]
  answers[r]+=1
  return answers[r]

N,R,Q=map(int,input().split())

l=[[]for i in range(N+1)]
for i in range(N-1):
  U,V=map(int,input().split())
  l[U].append(V)
  l[V].append(U)

children=[[]for i in range(N+1)] # 직계 자식들 보관
parent=[0 for i in range(N+1)] # 직계 부모 보관
root=[R]
while root:
  r=root.pop()
  for child in l[r]:
    if len(children[child])==0:
      children[r].append(child)
      parent[child]=r
      root.append(child)

answers=[0 for i in range(N+1)]
find(R)

for i in range(Q):
  U=int(input())
  print(answers[U])
