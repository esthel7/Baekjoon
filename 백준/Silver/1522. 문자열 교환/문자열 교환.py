import sys
input=sys.stdin.readline

l=list(input().rstrip())
cnt=0
start=-1
last=-1
loc=[]
for i in range(len(l)):
  if l[i]=='b':
    loc.append(i)
    cnt+=1
    if start==-1:
      start=i
    last=i

if cnt==0:
  print(0)
  exit()

l+=l
answer=-1
for item in loc:
  now=0
  for i in range(item,item+cnt):
    if l[i]!='b':
      now+=1
  if answer==-1 or answer>now:
    answer=now
    if answer==0:
      break

print(answer)
