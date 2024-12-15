import sys
input=sys.stdin.readline

N=int(input())
l=list(map(int,input().split()))
l.sort()

answer=[-1,[]]
for i in range(N-2):
  left=i+1
  right=N-1
  while left<right:
    now=l[i]+l[left]+l[right]
    if answer[0]==-1 or answer[0]>abs(now):
      answer=[abs(now),[l[i],l[left],l[right]]]
    if now==0:
      print(l[i],l[left],l[right])
      exit()
    elif now>0:
      right-=1
    else:
      left+=1

print(answer[1][0],answer[1][1],answer[1][2])
