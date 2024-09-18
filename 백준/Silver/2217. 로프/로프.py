import sys
input=sys.stdin.readline

N=int(input())
l=[]
for i in range(N):
  l.append(int(input()))
l.sort()

answer=0
for i in range(N):
  answer=max(answer,l[i]*(N-i))

print(answer)
