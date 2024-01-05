import sys
input=sys.stdin.readline

n=int(input())
l=[]
for i in range(n):
  l.append(int(input()))

answer=[] # 정답 배열
prints=[] # 출력
save=[] # 배열에 보관
now=1 # 배열에 넣을 수
flag=True
for i in range(len(l)):
  if l[i]>=now:
    for j in range(now,l[i]+1):
      save.append(j)
      prints.append('+')
    now=l[i]+1
    answer.append(save.pop())
    prints.append('-')
  else:
    if len(save) and save[-1]==l[i]:
      answer.append(save.pop())
      prints.append('-')
    else:
      print('NO')
      flag=False
      break

if flag:
  for now in prints:
    print(now)
