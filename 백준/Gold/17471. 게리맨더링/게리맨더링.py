import sys
input=sys.stdin.readline

def linked(now):
  if not now:
    return False

  q=[now[0]]
  left={}
  for key in now:
    left[key]=True
  left.pop(q[0])

  while q:
    item=q.pop()
    for node in graph[item].keys():
      if node in left:
        left.pop(node)
        q.append(node)

  if not left.keys():
    return True
  return False


def calculate(now):
  if not now:
    return True

  global answer
  visited=[False for i in range(N+1)]
  first=0
  for key in now:
    visited[key]=True
    first+=l[key]

  if not linked(now):
    return True

  checkNow=[]
  second=0
  for i in range(1,N+1):
    if not visited[i]:
      checkNow.append(i)
      second+=l[i]

  if not linked(checkNow):
    return True

  value=first-second
  if value<0:
    if answer==-1:
      answer=-value
    else:
      answer=min(answer,-value)
    return True
  else:
    if answer==-1:
      answer=value
    else:
      answer=min(answer,value)
    return False


def make(now,start):
  if not calculate(now):
    return
  elif not now and start>=N//2+1:
    return

  for i in range(start,N+1):
    now.append(i)
    make(now,i+1)
    now.pop()


N=int(input())
l=[0]+list(map(int,input().split()))
graph={}
root=[0 for i in range(N+1)]
cnt=N
for i in range(1,N+1):
  graph[i]={}
  now=list(map(int,input().split()))
  for j in range(1,len(now)):
    graph[i][now[j]]=True
    if root[i]==0:
      if root[now[j]]==0:
        root[i]=i
        root[now[j]]=i
        cnt-=1
      else:
        root[i]=root[now[j]]
        cnt-=1
    else:
      if root[now[j]]==0:
        root[now[j]]=root[i]
        cnt-=1
      elif root[i]!=root[now[j]]:
        Min=min(root[now[j]],root[i])
        Max=max(root[now[j]],root[i])
        if Min==Max:
          continue
        cnt-=1
        for k in range(1,N+1):
          if root[k]==Max:
            root[k]=Min

answer=-1

if cnt>2:
  print(-1)
  exit(0)
elif cnt==1:
  make([],1)
else:
  if N==2:
    print(abs(l[1]-l[2]))
    exit(0)
  now=[]
  for i in range(1,N+1):
    if root[i]==root[1]:
      now.append(i)
  calculate(now)

print(answer)
