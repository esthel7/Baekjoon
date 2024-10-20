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

answer=''
for i in range(num0//2):
  answer+='0'
for i in range(num1//2):
  answer+='1'

print(answer)
