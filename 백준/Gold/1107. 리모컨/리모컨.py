import sys
input=sys.stdin.readline

N=int(input())
M=int(input())
l=[]
if M>0:
  l=list(input().rstrip().split())
no={}
for idx in l:
  if idx=='+' or idx=='-':
    no[idx]=True
    continue
  no[int(idx)]=True

if N==100:
  print(0)
  exit()

q=[[100,0]]
last=len(str(N))

have=[[0,last-1]]
for i in range(10):
  if i not in no:
    have.append([i,last-1])
for i in range(9,-1,-1):
  if i not in no:
    have.append([i,last-3])

while have:
  now,num=have.pop() # 현재 수, 조작할 자릿수
  if num<=-1:
    q.append([now,len(str(now))])
    continue

  left=(N-now*(10**(num+1)))//(10**num)
  if left>=10:
    for i in range(9,-1,-1):
      if i not in no:
        now=now*10+i
        break
    have.append([now,num-1])
  elif left<0:
    for i in range(10):
      if i not in no:
        have.append([now*10+i,num-1])
        break
  else:
    if left not in no:
      have.append([now*10+left,num-1])
    for i in range(left+1,10):
      if i not in no:
        have.append([now*10+i,num-1])
        break
    for i in range(left-1,-1,-1):
      if i not in no:
        have.append([now*10+i,num-1])
        break


answer=-1
for num,cnt in q:
  if '+' in no and num<N:
    continue
  if '-' in no and num>N:
    continue
  value=abs(N-num)+cnt
  if answer==-1 or answer>value:
    answer=value

print(answer)
