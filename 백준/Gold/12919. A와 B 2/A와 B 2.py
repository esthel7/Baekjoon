import sys
from collections import deque
input=sys.stdin.readline

S=deque(input().rstrip())
T=deque(input().rstrip())

lenS=len(S)
lenT=len(T)

reverseS=deque([])
for i in range(lenS-1,-1,-1):
  reverseS.append(S[i])

if T[0]=='B':
  if T[-1]=='B':
    q=deque([[deque(T),lenT,True]])
  else:
    q=deque([[deque(T),lenT,True],[deque(T),lenT,False]]) # true면 뒤에서 빼기
else:
  q=deque([[deque(T),lenT,True]])

while q:
  t,lent,flag=q.popleft()
  # print('t=',t,flag)
  if lent==lenS:
    if (flag and t==S) or (not flag and t==reverseS):
      print(1)
      exit(0)
    continue

  if flag:
    if t[-1]=='A':
      t.pop()
      q.append([deque(t),lent-1,True])
      t.append('A')
    if t[0]=='B':
      t.popleft()
      q.append([deque(t),lent-1,False])
  else:
    if t[0]=='A':
      t.popleft()
      q.append([deque(t),lent-1,False])
      t.appendleft('A')
    if t[-1]=='B':
      t.pop()
      q.append([deque(t),lent-1,True])

print(0)


