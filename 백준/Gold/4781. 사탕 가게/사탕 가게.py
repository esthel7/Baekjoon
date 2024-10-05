import sys
input=sys.stdin.readline

while True:
  n,m=map(float,input().split())
  if n==0:
    break

  n=int(n)
  m=int(m*100)

  answer=-1
  money=[0 for i in range(m+1)]
  for i in range(n):
    c,p=map(float,input().split())
    c=int(c)
    p=int(p*100+0.5)
    if p>m:
      continue
    for j in range(p,m+1):
      money[j]=max(money[j],money[j-p]+c)
      answer=max(answer,money[j])

  print(answer)

