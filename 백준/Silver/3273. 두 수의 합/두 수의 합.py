import sys
input=sys.stdin.readline

n=int(input())
l=list(map(int,input().split()))
x=int(input())

l.sort()
cnt=0
start=0
end=n-1
while start!=end:
  now=l[start]+l[end]
  if now==x:
    cnt+=1
    start+=1
  elif now>x:
    end-=1
  else:
    start+=1
print(cnt)
