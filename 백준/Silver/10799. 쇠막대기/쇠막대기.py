l=list(input().rstrip())

cnt=0
stick=[]
i=0
while i!=len(l):
  if l[i]=='(' and l[i+1]==')':
    cnt+=len(stick)
    i+=2
    continue

  if l[i]=='(':
    stick.append(1)
  else:
    stick.pop()
    cnt+=1
  i+=1
print(cnt)
