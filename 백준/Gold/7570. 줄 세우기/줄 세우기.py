import sys
input=sys.stdin.readline

N=int(input())
l=list(map(int,input().split()))

s=[0 for i in range(N+1)]

for i in range(N):
  now=l[i]
  s[now]=s[now-1]+1

print(N-max(s))
