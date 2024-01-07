import sys
input=sys.stdin.readline

def find(l):
  s=[]
  for i in range(len(l)):
    if s:
      check=s[-1]
      if check==l[i]:
        s.pop()
        continue
      else:
        s.append(l[i])
    else:
      s.append(l[i])
  
  if s:
    return 0
  return 1

N=int(input())
l=[]
cnt=0
for i in range(N):
  l.append(list(input().rstrip()))
  cnt+=find(l[i])
print(cnt)
