import sys
input=sys.stdin.readline

N,L=map(int,input().split())
l=list(map(int,input().split()))
l.sort(reverse=True)

cnt=1
now=l.pop()
while l:
  item=l.pop()
  if now+L-1>=item:
    continue
  cnt+=1
  now=item

print(cnt)
