import sys
input=sys.stdin.readline

N=int(input())

info={}
for i in range(1,N+1):
  info[i]=[]

for i in range(N-1):
  a,b=map(int,input().split())
  info[a].append(b)
  info[b].append(a)

q=[1]
answer=[0 for i in range(N+1)]
while q:
  parent=q.pop()
  for child in info[parent]:
    if not answer[child]:
      answer[child]=parent
      q.append(child)

for i in range(2,N+1):
  print(answer[i])
