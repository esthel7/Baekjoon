import sys
input=sys.stdin.readline

def possible(x,y,k):
  for i in range(x,x+k+1):
    for j in range(y,y+k+1):
      if l[i][j]==0:
        return False
  return True


def change(x,y,k,num):
  for i in range(x,x+k+1):
    for j in range(y,y+k+1):
      l[i][j]=num


def find(now):
  global answer
  if answer!=-1 and answer==now:
    return

  for i in range(10):
    for j in range(10):
      if l[i][j]==1:
        for k in range(4,-1,-1):
          if boxes[k]>0 and i+k<10 and j+k<10 and possible(i,j,k):
            boxes[k]-=1
            change(i,j,k,0)
            find(now+1)
            boxes[k]+=1
            change(i,j,k,1)
        return

  if answer==-1 or answer>now:
    answer=now

l=[]
for i in range(10):
  l.append(list(map(int,input().split())))

answer=-1
boxes=[5,5,5,5,5]
find(0)
print(answer)
