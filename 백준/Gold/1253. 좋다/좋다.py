import sys
input=sys.stdin.readline

N=int(input())
l=list(map(int,input().split()))
l.sort()

answer=0
for i in range(N):
  goal=l[i]
  start=0
  end=N-1
  while start<end:
    now=l[start]+l[end]
    if now==goal:
      if start==i:
        start+=1
      elif end==i:
        end-=1
      else:
        answer+=1
        break
    elif now>goal:
      end-=1
    else:
      start+=1

print(answer)
