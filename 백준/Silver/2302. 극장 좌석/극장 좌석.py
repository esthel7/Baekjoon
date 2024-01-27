import sys
input=sys.stdin.readline

def find(P):
  l=[0 for i in range(P+2)]
  l[0]=1
  for i in range(2,P+2):
    l[i]=l[i-1]+l[i-2]
  return sum(l)

N=int(input())
M=int(input())
vip=[]
for i in range(M):
  vip.append(int(input()))

answer=1
possible=[]
for i in range(1,N):
  if i+1 not in vip and i not in vip:
    possible.append([i,i+1])
  else:
    P=len(possible)
    if P!=0:
      answer*=find(P)
    possible=[]

P=len(possible)
if P!=0:
  answer*=find(P)

print(answer)
