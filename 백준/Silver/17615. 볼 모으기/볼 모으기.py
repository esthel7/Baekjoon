import sys
input=sys.stdin.readline

N=int(input())
l=input().rstrip()

last=l[-1]
end=N
for i in range(N-1,-1,-1):
  if l[i]==last:
    end-=1
  else:
    break

if not end:
  print(0)
  exit(0)

R=0
B=0
for i in range(end):
  if l[i]=='R':
    R+=1
  else:
    B+=1

answer=min(R,B)

first=l[0]
start=0
for i in range(N):
  if l[i]==first:
    start+=1
  else:
    break

R=0
B=0
for i in range(start,N):
  if l[i]=='R':
    R+=1
  else:
    B+=1

answer=min(answer,min(R,B))
print(answer)
