import sys
input=sys.stdin.readline

def check(now):
  if now==0:
    cnt0[0]+=1
  elif now==1:
    cnt1[0]+=1
  else:
    cntM1[0]+=1

def find(N):
  xbox=[0,0,0,1,1,1,2,2,2]
  ybox=[0,1,2,0,1,2,0,1,2]
  q=[]
  q.append([N,0,0])
  while q:
    [N,x,y]=q.pop()
    if N==1:
      check(l[x][y])
      continue

    first=l[x][y]
    breakFlag=False
    for i in range(x,x+N):
      for j in range(y,y+N):
        if l[i][j]!=first:
          breakFlag=True
          break
      if breakFlag:
        break
    if not breakFlag:
      check(first)
    else:
      newN=N//3
      for i in range(9):
        q.append([newN,x+xbox[i]*newN,y+ybox[i]*newN])

N=int(input())
l=[]
for i in range(N):
  l.append(list(map(int,input().split())))

cntM1=[0]
cnt0=[0]
cnt1=[0]
find(N)
print(cntM1[0])
print(cnt0[0])
print(cnt1[0])
