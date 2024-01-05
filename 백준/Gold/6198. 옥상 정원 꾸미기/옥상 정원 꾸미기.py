import sys
input=sys.stdin.readline

n=int(input())
l=[]
for i in range(n):
  l.append(int(input()))

cnt=0
s=[l[0]]
for i in range(1,n):
  now=l[i]
  while len(s):
    a=s.pop()
    if a<=now:
      continue
    else:
      s.append(a)
      cnt+=len(s)
      s.append(now)
      break

  if len(s)==0:
    s.append(now)

print(cnt)
