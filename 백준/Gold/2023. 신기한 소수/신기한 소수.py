import sys
input=sys.stdin.readline

def check(value):
  for i in range(2,int(value**(0.5))+1):
    if value%i==0:
      return False
  return True

N=int(input())

num=[2,3,5,7]
if N==1:
  for item in num:
    print(item)
  exit()

plus=[1,3,7,9]
idx=1
while idx<N:
  idx+=1
  newNum=[]
  for item in num:
    for p in plus:
      value=item*10+p
      if check(value):
        newNum.append(value)
  num=list(newNum)

for item in num:
  print(item)

