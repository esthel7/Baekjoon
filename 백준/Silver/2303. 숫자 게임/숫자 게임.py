import sys
input=sys.stdin.readline

def find(l,start,idx):
  global answer
  if len(l)==3:
    value=sum(l)%10
    if answer[0]<value:
      answer=[value,idx]
    elif answer[0]==value and answer[1]<idx:
      answer[1]=idx
    return
  for i in range(start,5):
    l.append(now[i])
    find(l,i+1,idx)
    l.pop()


N=int(input())
answer=[0,0]
for i in range(N):
  now=list(map(int,input().split()))
  find([],0,i+1)

print(answer[1])
