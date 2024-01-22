import sys
input=sys.stdin.readline

def link(num):
  check=[[arr,[-1,-1]] for arr in num]
  root=0

  for t in range(7):
    x=check[t][0][0]
    y=check[t][0][1]
    if check[t][1][0]==-1:
      check[t][1]=[x,y]
      root+=1
      rootX=x
      rootY=y
    else:
      rootX=check[t][1][0]
      rootY=check[t][1][1]

    for i in range(4):
      if 0<=x+xbox[i]<5 and 0<=y+ybox[i]<5 and [x+xbox[i],y+ybox[i]] in num:
        for j in range(7):
          if check[j][0][0]==x+xbox[i] and check[j][0][1]==y+ybox[i]:
            if check[j][1][0]==-1:
              check[j][1]=[rootX,rootY]
            elif check[j][1][0]!=rootX or check[j][1][1]!=rootY:
              prevX=check[j][1][0]
              prevY=check[j][1][1]
              root-=1
              for k in range(7):
                if check[k][1][0]==prevX and check[k][1][1]==prevY:
                  check[k][1]=[rootX,rootY]
            break

  if root==1:
    return True
  return False


def find(start,num,Y):
  if Y==4:
    return

  if len(num)==7:
    if link(num):
      total[0]+=1
    return

  for i in range(start,25):
    num.append([i//5,i%5])
    if l[i//5][i%5]=='Y':
      find(i+1,num,Y+1)
    else:
      find(i+1,num,Y)
    num.pop()


l=[]
for i in range(5):
  l.append(list(input().rstrip()))

xbox=[-1,1,0,0]
ybox=[0,0,-1,1]

total=[0]
find(0,[],0)
print(total[0])
