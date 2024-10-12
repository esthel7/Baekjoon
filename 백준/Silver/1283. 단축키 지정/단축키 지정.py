import sys
input=sys.stdin.readline

N=int(input())
info={}
for i in range(N):
  now=list(input().rstrip().split())
  flag=False
  for j in range(len(now)):
    word=now[j]
    change=word[0].upper()
    if change in info:
      continue
    info[change]=True
    flag=True
    now[j]='['+now[j][0]+']'+now[j][1:]
    break

  if not flag:
    for j in range(len(now)):
      for k in range(1,len(now[j])):
        change=now[j][k].upper()
        if change in info:
          continue
        info[change]=True
        now[j]=now[j][:k]+'['+now[j][k]+']'+now[j][k+1:]
        flag=True
        break
      if flag:
        break

  print(' '.join(now))

