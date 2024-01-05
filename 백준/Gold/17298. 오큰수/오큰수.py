N=int(input())
l=list(map(int,input().split()))

s=[]
answer=[-1 for i in range(N)]
for i in range(N):
  now=l[i]
  if not len(s):
    s.append([now,i])
    continue
  while len(s):
    if s[-1][0]<now:
      [value,idx]=s.pop()
      answer[idx]=now
    else:
      s.append([now,i])
      break
  if not len(s):
    s.append([now,i])

for i in range(N):
  print(answer[i],end=' ')
