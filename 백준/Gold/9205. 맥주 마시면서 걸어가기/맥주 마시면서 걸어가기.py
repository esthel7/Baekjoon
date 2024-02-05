import sys
input=sys.stdin.readline

# 50m에 한병
# 빈병 버리고 새로 살 수 있고 max는 20

def find(x,y):
  q=[[20,x,y]]
  while q:
    cnt,x,y=q.pop()
    if abs(rock[0]-x)+abs(rock[1]-y)<=50*cnt:
      print('happy')
      return
    i=0
    while i<len(l):
      if abs(l[i][0]-x)+abs(l[i][1]-y)<=50*cnt:
        q.append([20,l[i][0],l[i][1]])
        l.pop(i)
        continue
      i+=1
  print('sad')

t=int(input())
for i in range(t):
  n=int(input())
  l=[]
  x,y=map(int,input().split())
  l=[]
  for j in range(1,n+1):
    l.append(list(map(int,input().split())))
  rock=list(map(int,input().split()))
  find(x,y)
