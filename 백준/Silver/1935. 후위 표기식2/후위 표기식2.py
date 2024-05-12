import sys
input=sys.stdin.readline

N=int(input())
l=list(input().rstrip())
num={}

for i in range(N):
  now=chr(ord('A')+i)
  num[now]=int(input())

cal=['+','-','*','/']
save=[]
for i in range(len(l)):
  if l[i] not in cal and 'A'<=l[i]<='Z':
    l[i]=num[l[i]]
  if l[i] not in cal:
    save.append(l[i])
  else:
    second=save.pop()
    first=save.pop()
    if l[i]=='+':
      save.append(first+second)
    elif l[i]=='-':
      save.append(first-second)
    elif l[i]=='*':
      save.append(first*second)
    else: # /
      save.append(first/second)

print('%.02f'%save[0])
