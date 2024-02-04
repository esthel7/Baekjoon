import sys
input=sys.stdin.readline

N=int(input())
first=[]
for i in range(N):
  first.append(int(input()))

prev=first[-1]
l=[arr for arr in first]
cnt=0
for i in range(N-2,-1,-1):
  if prev<=l[i]:
    cnt+=l[i]-prev+1
    l[i]=prev-1
  prev=l[i]
print(cnt)
