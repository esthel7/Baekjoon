import sys
input=sys.stdin.readline

N=int(input())
l=[]
for i in range(N):
  l.append(int(input()))

l.sort()
s=set()
for i in range(N):
  for j in range(N):
    s.add(l[i]+l[j])

S=len(s)

for i in range(N-1,-1,-1):
  for j in range(N):
    total=l[i]-l[j]
    if total in s:
      print(l[i])
      exit(0)

