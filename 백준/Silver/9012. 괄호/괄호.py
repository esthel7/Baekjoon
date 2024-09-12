import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
  now=list(input().rstrip())
  stack=[]
  flag=False
  for i in range(len(now)):
    if now[i]=='(':
      stack.append(i)
    else:
      if stack:
        stack.pop()
      else:
        print('NO')
        flag=True
        break
  if flag:
    continue
  if stack:
    print('NO')
  else:
    print('YES')
