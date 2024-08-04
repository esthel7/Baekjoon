import sys
input=sys.stdin.readline

def find(startx,starty,endx,endy):
  global white,blue
  flag=l[startx][starty]
  for i in range(startx,endx):
    for j in range(starty,endy):
      if l[i][j]!=flag:
        diff=(endx-startx)//2
        find(startx,starty,endx-diff,endy-diff)
        find(startx+diff,starty,endx,endy-diff)
        find(startx,starty+diff,endx-diff,endy)
        find(startx+diff,starty+diff,endx,endy)
        return
  if flag==0:
    # print('white',startx,starty,endx,endy)
    white+=1
  else:
    # print('blue',startx,starty,endx,endy)
    blue+=1


N=int(input())
l=[]
for i in range(N):
  l.append(list(map(int,input().split())))

white=0
blue=0
find(0,0,N,N)

print(white)
print(blue)
