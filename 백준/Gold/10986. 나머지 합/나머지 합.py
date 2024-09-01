import sys
input=sys.stdin.readline

N,M=map(int,input().split())
l=list(map(int,input().split()))
info={}

total=[0 for i in range(N)]
total[0]=l[0]
info[l[0]%M]=[0]

for i in range(1,N):
  total[i]=total[i-1]+l[i]
  if total[i]%M in info:
    info[total[i]%M].append(i)
  else:
    info[total[i]%M]=[i]

answer=0
if 0 in info:
  answer+=len(info[0])
for keys in info.keys():
  now=len(info[keys])
  answer+=now*(now-1)//2

print(answer)
