n=int(input())
num=[[] for i in range(n+1)]
num[1]=[1]

for i in range(1,n+1):
  l=num[i]
  if len(l)==0:
    continue
  if i+1<=n:
    l.append(i+1)
    if len(num[i+1])==0 or len(num[i+1])>len(l):
      num[i+1]=list(l)
    l.pop()
  if i*2<=n:
    l.append(i*2)
    if len(num[i*2])==0 or len(num[i*2])>len(l):
      num[i*2]=list(l)
    l.pop()
  if i*3<=n:
    l.append(i*3)
    if len(num[i*3])==0 or len(num[i*3])>len(l):
      num[i*3]=list(l)
    l.pop()

l=num[n]
print(len(l)-1)
l.reverse()
for answer in l:
  print(answer,end=' ')
