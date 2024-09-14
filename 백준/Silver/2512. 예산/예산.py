import sys
input=sys.stdin.readline

N=int(input())
l=list(map(int,input().split()))
M=int(input())

l.sort()

answer=-1
for i in range(N):
  idx=N-i
  now=M//idx
  if now>=l[i]:
    M-=l[i]
  else:
    M-=now
    answer=now
    break

if answer==-1:
  print(l[-1])
else:
  print(answer)
