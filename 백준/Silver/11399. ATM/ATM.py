import sys
input=sys.stdin.readline

N=int(input())
l=list(map(int,input().split()))
l.sort()
for i in range(1,N):
  l[i]+=l[i-1]
print(sum(l))
