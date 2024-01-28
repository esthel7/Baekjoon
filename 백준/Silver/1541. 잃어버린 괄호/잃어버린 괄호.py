first=list(input().rstrip())

l=[]
number=0

for now in first:
  if now=='+':
    l.append(number)
    l.append('+')
    number=0

  elif now=='-':
    l.append(number)
    l.append('-')
    number=0

  else:
    now=int(now)
    if number==0:
      number=now
    else:
      number*=10
      number+=now
l.append(number)

number=0
save=[]
for i in range(len(l)-1,-1,-1):
  if l[i]=='+':
    continue
  if l[i]=='-':
    number*=(-1)
    save.append(number)
    number=0
  else:
    number+=l[i]
save.append(number)

print(sum(save))

