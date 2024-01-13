from collections import deque

def star(n,total):
  for i in range(0,n,3):
    for j in range(total):
      if l[i][j]=='*':
        l[i][j]='*'
        l[i+1][j-1]='*'
        l[i+1][j+1]='*'
        for k in range(5):
          l[i+2][j-2+k]='*'


def make(n,x,y):
  total=y*2
  q=deque([[x,y]])
  while q:
    [x,y]=q.popleft()
    l[x][y]='*'

    if x+3!=n:
      if q and q[-1][0]==x+3 and q[-1][1]==y-3:
        q.pop()
        q.append([x+3,y+3])
        continue
      q.append([x+3,y-3])
      q.append([x+3,y+3])

  star(n,total)

n=int(input())
m=n//3

l=[[' ' for i in range(5*m+m-1)]for j in range(n)]

half=(5*m+m-1)//2
make(n,0,half)
for i in range(n):
  print(''.join(l[i]))
