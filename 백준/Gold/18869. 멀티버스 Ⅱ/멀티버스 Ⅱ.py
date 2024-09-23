import sys
input=sys.stdin.readline

M,N=map(int,input().split())
items={}
info={}
for i in range(M):
  now=list(map(int,input().split()))

  check=''
  for j in range(N):
    check+=str(now[j])+'-'
  if check in items:
    continue
  items[check]=True

  ranks=['' for i in range(N)]
  sortedNow=sorted(now)
  idx={}
  for j in range(N):
    idx[sortedNow[j]]=j
  
  for j in range(N):
    ranks[j]=str(idx[now[j]])

  name='-'.join(ranks)
  if name in info:
    info[name]+=1
  else:
    info[name]=1

answer=0
for name in info.keys():
  if info[name]>=2:
    answer+=info[name]*(info[name]-1)//2

print(answer)
