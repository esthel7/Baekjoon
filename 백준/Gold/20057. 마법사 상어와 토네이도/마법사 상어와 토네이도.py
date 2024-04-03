import sys
import math
input=sys.stdin.readline

def move(prevx,prevy,nowx,nowy):
  left=0
  now=l[nowx][nowy]
  l[nowx][nowy]=0
  now1=math.floor(now*0.01)
  now2=math.floor(now*0.02)
  now5=math.floor(now*0.05)
  now7=math.floor(now*0.07)
  now10=math.floor(now*0.1)
  nowa=now-(now1*2+now2*2+now5+now7*2+now10*2)

  if prevx==nowx and prevy-1==nowy: # left
    if nowx-2>=0:
      l[nowx-2][nowy]+=now2
    else:
      left+=now2

    if nowx-1>=0:
      if nowy-1>=0:
        l[nowx-1][nowy-1]+=now10
      else:
        left+=now10
      l[nowx-1][nowy]+=now7
      l[nowx-1][nowy+1]+=now1
    else:
      left+=now10+now7+now1

    if nowy-2>=0:
      l[nowx][nowy-2]+=now5
      l[nowx][nowy-1]+=nowa
    else:
      left+=now5
      if nowy-1>=0:
        l[nowx][nowy-1]+=nowa
      else:
        left+=nowa

    if nowx+1<N:
      if nowy-1>=0:
        l[nowx+1][nowy-1]+=now10
      else:
        left+=now10
      l[nowx+1][nowy]+=now7
      l[nowx+1][nowy+1]+=now1
    else:
      left+=now10+now7+now1

    if nowx+2<N:
      l[nowx+2][nowy]+=now2
    else:
      left+=now2

  elif prevx==nowx and prevy+1==nowy: # right
    if nowx-2>=0:
      l[nowx-2][nowy]+=now2
    else:
      left+=now2

    if nowx-1>=0:
      if nowy+1<N:
        l[nowx-1][nowy+1]+=now10
      else:
        left+=now10
      l[nowx-1][nowy]+=now7
      l[nowx-1][nowy-1]+=now1
    else:
      left+=now10+now7+now1

    if nowy+2<N:
      l[nowx][nowy+2]+=now5
      l[nowx][nowy+1]+=nowa
    else:
      left+=now5
      if nowy+1<N:
        l[nowx][nowy+1]+=nowa
      else:
        left+=nowa

    if nowx+1<N:
      if nowy+1<N:
        l[nowx+1][nowy+1]+=now10
      else:
        left+=now10
      l[nowx+1][nowy]+=now7
      l[nowx+1][nowy-1]+=now1
    else:
      left+=now10+now7+now1

    if nowx+2<N:
      l[nowx+2][nowy]+=now2
    else:
      left+=now2

  elif prevx-1==nowx and prevy==nowy: # top
    if nowx-2>=0:
      l[nowx-2][nowy]+=now5
    else:
      left+=now5

    if nowx-1>=0:
      if nowy-1>=0:
        l[nowx-1][nowy-1]+=now10
      else:
        left+=now10
      l[nowx-1][nowy]+=nowa
      if nowy+1<N:
        l[nowx-1][nowy+1]+=now10
      else:
        left+=now10
    else:
      left+=now10+nowa+now10

    if nowy-2>=0:
      l[nowx][nowy-2]+=now2
      l[nowx][nowy-1]+=now7
    else:
      left+=now2
      if nowy-1>=0:
        l[nowx][nowy-1]+=now7
      else:
        left+=now7
    if nowy+2<N:
      l[nowx][nowy+2]+=now2
      l[nowx][nowy+1]+=now7
    else:
      left+=now2
      if nowy+1<N:
        l[nowx][nowy+1]+=now7
      else:
        left+=now7

    if nowy-1>=0:
      l[nowx+1][nowy-1]+=now1
    else:
      left+=now1
    if nowy+1<N:
      l[nowx+1][nowy+1]+=now1
    else:
      left+=now1

  elif prevx+1==nowx and prevy==nowy: # down
    if nowy-1>=0:
      l[nowx-1][nowy-1]+=now1
    else:
      left+=now1
    if nowy+1<N:
      l[nowx-1][nowy+1]+=now1
    else:
      left+=now1

    if nowy-2>=0:
      l[nowx][nowy-2]+=now2
      l[nowx][nowy-1]+=now7
    else:
      left+=now2
      if nowy-1>=0:
        l[nowx][nowy-1]+=now7
      else:
        left+=now7
    if nowy+2<N:
      l[nowx][nowy+2]+=now2
      l[nowx][nowy+1]+=now7
    else:
      left+=now2
      if nowy+1<N:
        l[nowx][nowy+1]+=now7
      else:
        left+=now7

    if nowx+1<N:
      if nowy-1>=0:
        l[nowx+1][nowy-1]+=now10
      else:
        left+=now10
      l[nowx+1][nowy]+=nowa
      if nowy+1<N:
        l[nowx+1][nowy+1]+=now10
      else:
        left+=now10
    else:
      left+=now10+nowa+now10

    if nowx+2<N:
      l[nowx+2][nowy]+=now5
    else:
      left+=now5

  return left

N=int(input())
l=[]
for i in range(N):
  l.append(list(map(int,input().split())))

prevx=N//2
prevy=N//2
line=1
answer=0
while True:
  if prevy-line<0:
    for i in range(prevy-1,-1,-1):
      answer+=move(prevx,prevy,nowx,i)
      prevx=nowx
      prevy=i
    print(answer)
    break

  nowx=prevx
  nowy=prevy-line
  for i in range(prevy-1,nowy-1,-1):
    answer+=move(prevx,prevy,nowx,i)
    prevx=nowx
    prevy=i

  nowx=prevx+line
  nowy=prevy
  for i in range(prevx+1,nowx+1):
    answer+=move(prevx,prevy,i,nowy)
    prevx=i
    prevy=nowy
  line+=1

  nowx=prevx
  nowy=prevy+line
  for i in range(prevy+1,nowy+1):
    answer+=move(prevx,prevy,nowx,i)
    prevx=nowx
    prevy=i

  nowx=prevx-line
  nowy=prevy
  for i in range(prevx-1,nowx-1,-1):
    answer+=move(prevx,prevy,i,nowy)
    prevx=i
    prevy=nowy
  line+=1
