import sys
input=sys.stdin.readline

answers=[]
for _ in range(3):
  N=int(input())

  total=0
  l=[]
  for i in range(N):
    num,cnt=map(int,input().split())
    l.append([num,cnt])
    total+=num*cnt

  if total%2!=0:
    answers.append(0)
    continue
  l.sort(reverse=True)

  Half=total//2
  if l[0][0]>Half:
    answers.append(0)
    continue

  success=False
  info={}
  for i in range(N):
    now=l[i][0]

    List=list(info.keys())
    List.sort()
    for j in range(1,l[i][1]+1):
      value=now*j
      if value==Half:
        success=True
        break
      elif value>Half:
        break

      for key in List:
        if key+value==Half:
          success=True
          break
        if key+value>Half:
          break
        info[key+value]=True

      if success:
        break

    if success:
      break

    for j in range(1,l[i][1]+1):
      if now*j>Half:
        break
      info[now*j]=True

  if success:
    answers.append(1)
  else:
    answers.append(0)

for answer in answers:
  print(answer)