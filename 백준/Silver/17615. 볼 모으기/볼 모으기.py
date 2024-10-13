import sys
input=sys.stdin.readline

N=int(input())
l=list(input().rstrip())

last=l[-1]
for i in range(N-1,-1,-1):
  if l[i]==last:
    N-=1
  else:
    break

if not N:
  print(0)
  exit(0)

R=0
B=0
for i in range(N):
  if l[i]=='R':
    R+=1
  else:
    B+=1

print(min(R,B))
