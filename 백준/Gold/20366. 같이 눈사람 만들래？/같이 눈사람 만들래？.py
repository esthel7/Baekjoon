import sys
input=sys.stdin.readline

N=int(input())
l=list(map(int,input().split()))
l.sort()

answer=-1

def check(start,end):
  if start>=end:
    return
  if start in info:
    if end in info[start]:
      return
    info[start][end]=True
    q.append([start,end])
    return
  else:
    info[start]={end:True}
    q.append([start,end])
    return

info={0:{N-1:True}}
q=[[0,N-1]]
while q:
  [start,end]=q.pop()
  left=start+1
  right=end-1
  while left<right:
    value=(l[start]+l[end])-(l[left]+l[right])
    if value==0:
      print(0)
      exit()
    elif value>0:
      left+=1
    else:
      value*=-1
      right-=1
    if answer==-1 or answer>value:
      answer=value
  check(start+1,end)
  check(start,end-1)

print(answer)

# 6, 10, 10, 28, 47, 60, 62, 62, 67, 70, 73, 100
