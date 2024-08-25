import sys
input=sys.stdin.readline

N=int(input())
l=list(map(int,input().split()))
l=sorted(l)

diff=abs(l[0]+l[N-1]-l[1]-l[N-2])

for i in range(N-3):
  for j in range(i+3,N):
    fix=l[i]+l[j]
    left=i+1
    right=j-1
    while left<right:
      now=l[left]+l[right]
      diff=min(diff,abs(now-fix))
      if now-fix==0:
        print(0)
        exit(0)
      elif now-fix>0:
        right-=1
      else:
        left+=1

print(diff)
