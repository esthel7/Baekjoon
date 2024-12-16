import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

l=[]
# while True:
#   now=input()
#   if now=='\n':
#     break
#   l.append(int(now))
while True:
  try:
    x=int(input())
    l.append(x)
  except:
    break

def find(idx,last):
  if idx==last:
    return
  now=l[idx]
  flag=-1
  for i in range(idx+1,last):
    if now>l[i]:
      continue
    else:
      flag=i
      break
  if flag==-1:
    find(idx+1,last)
  else:
    find(idx+1,flag)
    find(flag,last)
  print(l[idx])

find(0,len(l))
