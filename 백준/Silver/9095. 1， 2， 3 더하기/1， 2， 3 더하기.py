import sys
input=sys.stdin.readline

def find(n):
  l=[0 for i in range(n+1)]
  l[0]=1
  for i in range(n+1):
    if i+1<=n:
      l[i+1]+=l[i]
    if i+2<=n:
      l[i+2]+=l[i]
    if i+3<=n:
      l[i+3]+=l[i]
  return l[n]


T=int(input())
for i in range(T):
  value=find(int(input()))
  print(value%1000000009)
