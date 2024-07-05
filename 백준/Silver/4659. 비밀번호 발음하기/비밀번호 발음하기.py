import sys
input=sys.stdin.readline

while True:
  now=list(input().rstrip())
  if now==['e','n','d']:
    break

  jcnt=0
  mcnt=0
  existflag=False
  if now[0] in ['a','e','i','o','u']:
    existflag=True
    mcnt=1
  else:
    jcnt=1

  flag=False
  for i in range(1,len(now)):
    if now[i-1]==now[i] and now[i] not in ['e','o']:
      flag=True
      break
    if now[i] in ['a','e','i','o','u']:
      existflag=True
      jcnt=0
      mcnt+=1
      if mcnt==3:
        flag=True
        break
    else:
      mcnt=0
      jcnt+=1
      if jcnt==3:
        flag=True
        break
  
  if not existflag or flag:
    print('<%s> is not acceptable.'%(''.join(now)))
  else:
    print('<%s> is acceptable.'%(''.join(now)))
