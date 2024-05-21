import sys
input=sys.stdin.readline

N=int(input())
s=[]
for i in range(N):
  command=input().rstrip().split()
  if len(command)==2: # push
    s.append(command[1])
  else:
    if command[0]=='pop':
      if len(s):
        print(s.pop())
      else:
        print(-1)
    elif command[0]=='size':
      print(len(s))
    elif command[0]=='empty':
      if len(s):
        print(0)
      else:
        print(1)
    else: # top
      if len(s):
        print(s[-1])
      else:
        print(-1)
