import sys
input=sys.stdin.readline

N,M=map(int,input().split())
info=[[]for i in range(N+1)]
for i in range(M):
  A,B=map(int,input().split())
  info[B].append(A)

answer=0
answers=[]
for i in range(1,N+1):
  visited=[False for i in range(N+1)]
  visited[i]=True
  cnt=1
  q=[i]
  while q:
    node=q.pop()
    for key in info[node]:
      if not visited[key]:
        visited[key]=True
        cnt+=1
        q.append(key)
  if answer<cnt:
    answer=cnt
    answers=[i]
  elif answer==cnt:
    answers.append(i)

for item in answers:
  print(item,end=' ')
print()
