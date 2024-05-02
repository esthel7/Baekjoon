import sys
input=sys.stdin.readline

def find(now,start):
  if len(now)==M:
    answer=''
    for i in range(M):
      answer+=str(l[now[i]])+' '
    if answer not in answers:
      answers[answer]=True
      print(answer)
    return
  for i in range(start,N):
    now.append(i)
    find(now,i+1)
    now.pop()

N,M=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
answers={}
find([],0)
