import sys
input=sys.stdin.readline

N,M,R=map(int,input().split())
l=[]
for i in range(N):
  l.append(list(map(int,input().split())))

board=[]
top=0
bottom=N
left=0
right=M
while True:
  now=[]
  for i in range(left,right):
    now.append(l[top][i])
  for i in range(top+1,bottom):
    now.append(l[i][right-1])
  for i in range(right-2,left-1,-1):
    now.append(l[bottom-1][i])
  for i in range(bottom-2,top,-1):
    now.append(l[i][left])
  top+=1
  bottom-=1
  left+=1
  right-=1
  board.append(now)
  if top==bottom or left==right:
    break

for i in range(len(board)):
  now=R%len(board[i])
  board[i]=board[i][now:]+board[i][:now]

top=0
bottom=N
left=0
right=M
idx=0
item=0
while True:
  for i in range(left,right):
    l[top][i]=board[idx][item]
    item+=1
  for i in range(top+1,bottom):
    l[i][right-1]=board[idx][item]
    item+=1
  for i in range(right-2,left-1,-1):
    l[bottom-1][i]=board[idx][item]
    item+=1
  for i in range(bottom-2,top,-1):
    l[i][left]=board[idx][item]
    item+=1
  top+=1
  bottom-=1
  left+=1
  right-=1
  idx+=1
  item=0
  if top==bottom or left==right:
    break

for i in range(N):
  for j in range(M):
    print(l[i][j],end=' ')
  print()
