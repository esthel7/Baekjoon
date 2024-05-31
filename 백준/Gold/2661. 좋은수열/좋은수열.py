import sys
input=sys.stdin.readline

def check(now):
  for i in range(len(now)-2,len(now)//2-1,-1):
    if now[i:]==now[i*2-len(now):i]:
      return False

  return True


def find(now):
  if len(now)==n:
    print(int(''.join(now)))
    exit(0)

  if len(now)==0:
    find(['1'])
  else:
    for i in range(1,4):
      if now[-1]==str(i):
        continue
      now.append(str(i))
      if check(now):
        find(now)
      now.pop()

n=int(input())
find([])
