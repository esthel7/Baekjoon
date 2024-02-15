import sys
input=sys.stdin.readline

N,K=map(int,input().split())
l=list(map(int,input().split()))

start=0
end=0
now=0
cnt=0
answer=0
while end<N:
  if l[end]%2==0:
    now+=1
    end+=1
  else:
    if cnt+1>K:
      if answer<now:
        answer=now
      while start<end:
        if l[start]%2==0:
          now-=1
          start+=1
        else:
          cnt-=1
          start+=1
          break
    else:
      cnt+=1
      end+=1
  # print('end!',start,end,'cnt=',cnt,'total=',now)

if answer<now:
  answer=now

print(answer)
