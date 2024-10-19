import sys
input=sys.stdin.readline

p,m=map(int,input().split())
info=[]
for i in range(p):
  l,n=input().rstrip().split()
  info.append([l,n])

if m==1:
  for l,n in info:
    print('Started!')
    print(l,n)
  exit(0)

room={}
for l,n in info:
  if not room:
    room[l+'-'+n]=[[n,l]]
    continue

  flag=False
  for key in room.keys():
    keyvalue=int(key.split('-')[0])
    if keyvalue-10<=int(l)<=keyvalue+10 and len(room[key])<m:
      room[key].append([n,l])
      flag=True
      break
  if not flag:
    room[l+'-'+n]=[[n,l]]

for key in room.keys():
  if len(room[key])==m:
    print('Started!')
  else:
    print('Waiting!')
  room[key].sort()
  for n,l in room[key]:
    print(l,n)
