import sys
input=sys.stdin.readline

N,game=input().rstrip().split()
names={}
for i in range(int(N)):
  now=input().rstrip()
  if now in names:
    continue
  names[now]=True

if game=='Y':
  print(len(names))
elif game=='F':
  print(len(names)//2)
else:
  print(len(names)//3)

