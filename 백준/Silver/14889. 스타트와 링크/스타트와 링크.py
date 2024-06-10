import sys
input=sys.stdin.readline

def calculate(left,right):
  global answer
  first=0
  second=0
  for i in range(Half):
    for j in range(i+1,Half):
      first+=l[left[i]][left[j]]+l[left[j]][left[i]]
  for i in range(Half):
    for j in range(i+1,Half):
      second+=l[right[i]][right[j]]+l[right[j]][right[i]]
  value=abs(first-second)
  if answer==-1 or answer>value:
    answer=value


def find(left,right,start):
  if start==N:
    if len(left)==Half and len(right)==Half:
      calculate(left,right)
    return

  if len(left)<Half:
    if len(left)==0 and start>=Half:
      return
    left.append(start)
    find(left,right,start+1)
    left.pop()
  if len(right)<Half:
    right.append(start)
    find(left,right,start+1)
    right.pop()


N=int(input())
l=[]
for i in range(N):
  l.append(list(map(int,input().split())))

Half=N//2
answer=-1
find([],[],0)
print(answer)
