import sys
input=sys.stdin.readline

N=int(input())
time=[0 for i in range(N+1)]
degrees=[0 for i in range(N+1)]
back=[[] for i in range(N+1)] # 해당 번호 후에 할 작업들 표시

for i in range(1,N+1):
  now=list(map(int,input().split()))
  time[i]=now[0]
  for j in range(2,2+now[1]):
    back[now[j]].append(i)
    degrees[i]+=1

working=[] # 작업중인 번호
for i in range(1,N+1):
  if degrees[i]==0:
    working.append(i) # 시작 가능한 작업들

answer=0
while True:
  pops=[]
  newWorking=[]
  for i in range(len(working)):
    now=working[i]
    time[now]-=1
    if time[now]==0:
      pops.append(i)
      for node in back[now]:
        degrees[node]-=1
        if degrees[node]==0:
          newWorking.append(node)

  answer+=1
  while pops:
    popidx=pops.pop()
    working.pop(popidx)

  for node in newWorking:
    working.append(node)
  
  if not working:
    break

print(answer)
