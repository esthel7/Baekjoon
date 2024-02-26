import sys
input=sys.stdin.readline

def find(start,now,num,N,M):
  if len(now)==M:
    check=''
    for item in now:
      check+=str(item)+' '
    if check in info:
      return
    info[check]=True
    print(check)
    return
  for i in range(start,N):
    if i in num:
      continue
    num.append(i)
    now.append(l[i])
    find(i+1,now,num,N,M)
    num.pop()
    now.pop()

info={}
N,M=map(int,input().split())
l=list(map(int,input().split()))
l.sort()

find(0,[],[],N,M)
