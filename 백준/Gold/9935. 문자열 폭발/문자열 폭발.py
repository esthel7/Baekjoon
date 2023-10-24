a=list(input())
b=list(input())
L=len(b)

s=[]
for i in range(len(a)):
  s.append(a[i])
  if s[-1]==b[-1]:
    sLen=len(s)
    if s[sLen-L:sLen]==b:
      for j in range(L):
        s.pop()
if len(s)==0:
  print('FRULA')
else:
  print(''.join(s))
