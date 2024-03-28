import sys
input=sys.stdin.readline

def find(l,flag):
  global answer
  L=len(l)
  for i in range(1,N):
    if flag:
      l.append(i)
      L+=1
      if now[i]==goal[i]:
        if L-2>=0 and l[L-2]==i-1:
          flag=False
        else:
          flag=True
      else:
        if L-2>=0 and l[L-2]==i-1:
          flag=True
        else:
          flag=False
    else:
      if now[i]==goal[i]:
        if L-1>=0 and l[L-1]==i-1:
          flag=True
        else:
          flag=False
      else:
        if L-1>=0 and l[L-1]==i-1:
          flag=False
        else:
          flag=True

  if not flag:
    if answer==-1 or answer>L:
      answer=L
    return


N=int(input())
now=list(input().rstrip())
goal=list(input().rstrip())

answer=-1
if now[0]==goal[0]:
  find([0],True)
  find([],False)
else:
  find([0],False)
  find([],True)
print(answer)
