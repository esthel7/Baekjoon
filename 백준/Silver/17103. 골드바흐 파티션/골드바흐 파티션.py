import sys
input=sys.stdin.readline

T=int(input())

l=[]
for i in range(T):
  l.append(int(input()))

Max=max(l)+1

sosu=[]
board=[True for i in range(Max)]
board[0]=False
board[1]=False
for i in range(2,Max):
  if board[i]:
    sosu.append(i)
    for j in range(i*2,Max,i):
      board[j]=False

for now in l:
  answer=0
  idx=0
  flag=now//2
  while True:
    if sosu[idx]>flag:
      break
    left=now-sosu[idx]
    if board[left]:
      answer+=1
    idx+=1

  print(answer)
