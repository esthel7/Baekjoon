import sys
input=sys.stdin.readline

def find():
  answer=-1
  for i in range(M):
    q=[]
    for j in range(3):
      q.append([0,i,0,j])

      while q:
        x,y,cnt,flag=q.pop()
        if x==N:
          if answer==-1 or answer>cnt:
            answer=cnt
          continue

        cnt+=l[x][y]
        if y-1>=0 and flag!=0:
          q.append([x+1,y-1,cnt,0])
        if y+1<M and flag!=1:
          q.append([x+1,y+1,cnt,1])
        if flag!=2:
          q.append([x+1,y,cnt,2])
  print(answer)


N,M=map(int,input().split())
l=[]
for i in range(N):
  l.append(list(map(int,input().split())))

find()
