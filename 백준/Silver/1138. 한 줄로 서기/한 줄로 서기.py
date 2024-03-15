import sys
import heapq
input=sys.stdin.readline

N=int(input())
l=list(map(int,input().split()))

degree=[]
changeFlag=False
for i in range(N):
  degree.append([l[i],i])
  if not changeFlag and l[i]==0:
    changeFlag=True
    start=i

answer=[]
while degree:
  value,idx=degree.pop(start)
  answer.append(idx+1)
  changeFlag=False
  for i in range(start):
    degree[i][0]-=1
    if not changeFlag and degree[i][0]==0:
      changeFlag=True
      start=i
  if not changeFlag:
    for i in range(start,len(degree)):
      if degree[i][0]==0:
        start=i
        break

for item in answer:
  print(item,end=' ')
