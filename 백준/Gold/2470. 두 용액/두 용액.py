import sys
input=sys.stdin.readline

N=int(input())
l=list(map(int,input().split()))
l.sort()

answer=[-1,[]]
left=0
right=len(l)-1

while left<right:
  now=l[left]+l[right]
  if now==0:
    print(l[left],l[right])
    exit(0)
  elif now>0:
    if answer[0]==-1 or answer[0]>now:
      answer=[now,[l[left],l[right]]]
    right-=1
  else:
    if answer[0]==-1 or answer[0]>-1*now:
      answer=[-1*now,[l[left],l[right]]]
    left+=1

print(answer[1][0],answer[1][1])
