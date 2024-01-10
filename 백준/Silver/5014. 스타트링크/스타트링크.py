from collections import deque

F,S,G,U,D=map(int,input().split())

visit=[False for i in range(F+1)]
q=deque([[S,0]])
doneFlag=False
while q:
  [now,cnt]=q.popleft()
  if visit[now]:
    continue
  visit[now]=True
  if now==G:
    print(cnt)
    doneFlag=True
    break
  if now+U<=F:
    q.append([now+U,cnt+1])
  if now-D>=1:
    q.append([now-D,cnt+1])

if not doneFlag:
  print('use the stairs')
