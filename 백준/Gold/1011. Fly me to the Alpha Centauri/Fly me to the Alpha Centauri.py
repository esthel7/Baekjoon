import sys
input=sys.stdin.readline

def find(diff):
  half=diff//2
  i=1
  now=0

  while now<=half:
    now+=i
    i+=1
  i-=1
  now-=i

  diff-=now*2 # 남은 값
  cnt=(i-1)*2
  if not diff:
    return cnt
  if diff>i:
    return cnt+2
  else:
    return cnt+1


T=int(input())
for i in range(T):
  x,y=map(int,input().split())
  print(find(y-x))
