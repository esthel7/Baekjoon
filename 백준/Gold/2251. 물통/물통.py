import sys
input=sys.stdin.readline

def find(a,b,c):
  name='%d-%d-%d'%(a,b,c)
  if name in visit:
    return
  visit[name]=True
  if a==0:
    answer[c]=True
  if a>0:
    if b+a<=B:
      find(0,a+b,c)
    elif b<B:
      move=B-b
      find(a-move,b+move,c)
    if c+a<=C:
      find(0,b,c+a)
    elif c<C:
      move=C-c
      find(a-move,b,c+move)
  if b>0:
    if b+a<=A:
      find(b+a,0,c)
    elif a<A:
      move=A-a
      find(a+move,b-move,c)
    if c+b<=C:
      find(a,0,c+b)
    elif c<C:
      move=C-c
      find(a,b-move,c+move)
  if c>0:
    if a+c<=A:
      find(a+c,b,0)
    elif a<A:
      move=A-a
      find(a+move,b,c-move)
    if c+b<=B:
      find(a,b+c,0)
    elif b<B:
      move=B-b
      find(a,b+move,c-move)

A,B,C=map(int,input().split())
answer={}
visit={}
find(0,0,C)
answer=sorted(answer.keys())
for item in answer:
  print(item,end=' ')
print()
