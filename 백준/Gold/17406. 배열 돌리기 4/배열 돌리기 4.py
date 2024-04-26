import sys
input=sys.stdin.readline

def makeNewMove(now):
  if len(now)==K:
    rotate(list(now))
    return
  for idx,r,c,s in move:
    if [idx,r,c,s] in now:
      continue
    now.append([idx,r,c,s])
    makeNewMove(now)
    now.pop()


def calculate(l):
  Min=-1
  for i in range(N):
    Sum=sum(l[i])
    if Min==-1 or Min>Sum:
      Min=Sum
  return Min


def rotate(now):
  global answer
  l=list(list(arr) for arr in board)
  for idx,r,c,s in now:
    top=r-s-1
    bottom=r+s
    left=c-s-1
    right=c+s

    while bottom-top>1:
      tmp=l[top][left]
      for i in range(bottom-top-1):
        l[top+i][left]=l[top+i+1][left]
      for i in range(right-left-1):
        l[bottom-1][left+i]=l[bottom-1][left+i+1]
      for i in range(bottom-top-1):
        l[bottom-1-i][right-1]=l[bottom-2-i][right-1]
      for i in range(right-left-1):
        l[top][right-1-i]=l[top][right-2-i]
      l[top][left+1]=tmp

      top+=1
      bottom-=1
      left+=1
      right-=1
  
  value=calculate(l)
  if answer==-1 or answer>value:
    answer=value


N,M,K=map(int,input().split())
board=[]
for _ in range(N):
  board.append(list(map(int,input().split())))

move=[]
for i in range(K):
  move.append([i]+list(map(int,input().split())))

answer=-1
makeNewMove([])

print(answer)
