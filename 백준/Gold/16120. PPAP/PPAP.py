import sys
input=sys.stdin.readline

def check():
  if s[-4]=='P' and s[-3]=='P' and s[-2]=='A' and s[-1]=='P':
    s.pop()
    s.pop()
    s.pop()

l=list(input().rstrip())
s=[]
for item in l:
  s.append(item)
  if len(s)>=4:
    check()

if len(s)==1 and s[0]=='P':
  print('PPAP')
else:
  print('NP')
