def find(N,r,c):
  q=[[N,0,0,0]]
  while q:
    [N,x,y,now]=q.pop()
    if N==2:
      for i in range(4):
        if x+xbox[i]==r and y+ybox[i]==c:
          print(now+i)
          break
    else:
      newN=N//2
      squareN=newN**2
      if x<=r<x+newN and y<=c<y+newN:
        q.append([newN,x,y,now])
      elif x<=r<x+newN and y+newN<=c<y+N:
        q.append([newN,x,y+newN,now+squareN])
      elif x+newN<=r<x+N and y<=c<y+newN:
        q.append([newN,x+newN,y,now+squareN*2])
      else:
        q.append([newN,x+newN,y+newN,now+squareN*3])


N,r,c=map(int,input().split())
N=pow(2,N) # 한 변의 길이
xbox=[0,0,1,1]
ybox=[0,1,0,1]

find(N,r,c)
