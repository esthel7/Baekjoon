import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
  n=int(input())

  l=[]
  info={}
  answer=False

  for i in range(n):
    l.append(list(input().rstrip()))

  l.sort(key=len)

  for now in l:
    if answer:
      break

    Now=len(now)
    if now[0] in info:
      move=info[now[0]]
      if move==True:
        answer=True
        continue
    else:
      if Now==1:
        info[now[0]]=True
      else:
        info[now[0]]={}
      move=info[now[0]]

    for j in range(1,Now):
      item=now[j]
      if item in move:
        if move[item]==True:
          answer=True
          break
        move=move[item]
      else:
        if j==Now-1:
          move[item]=True
          break
        move[item]={}
        move=move[item]

  if not answer:
    print('YES')
  else:
    print('NO')

