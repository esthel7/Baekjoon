import sys
input=sys.stdin.readline

S=list(input().rstrip())

num0=0
num1=0
for item in S:
  if item=='0':
    num0+=1
  else:
    num1+=1
num0//=2
num1//=2

cnt=0
for i in range(len(S)-1,-1,-1):
  if S[i]=='0':
    S.pop(i)
    cnt+=1
    if cnt==num0:
      break

cnt=0
i=0
while cnt<num1:
  if S[i]=='1':
    S.pop(i)
    cnt+=1
    continue
  i+=1

print(''.join(S))
