import sys
from collections import deque
input=sys.stdin.readline

def findMin(n):
  answer=''
  first=[2,5,4,6,3,7]
  second=[6,2,5,4,3,7]

  small=deque([])
  if n<7:
    answer=Min[n]
    if answer=='0':
      answer=6
    return answer

  for i in range(n//7):
    small.append(7)

  left=n%7
  if left==0:
    for i in range(len(small)):
      answer+=Min[small[i]]
      if answer=='0':
        answer='6'
    return answer

  if left==1:
    small.pop()
    small.appendleft(6)
    small.appendleft(2)
    for i in range(len(small)):
      answer+=Min[small[i]]
    return answer

  for firstitem in first:
    if firstitem==left:
      small.appendleft(left)
      for i in range(len(small)):
        answer+=Min[small[i]]
        if answer=='0':
          answer='6'
      return answer

    if firstitem>left:
      small.pop()
      small.appendleft(7-(firstitem-left))
      answer+=Min[firstitem]
      break

  while small:
    now=small.popleft()
    if now==7 or not small:
      answer+=Min[now]
      break

    for item in second:
      if item==now:
        answer+=Min[now]
        break

      if item>now:
        small.pop()
        small.appendleft(7-(item-now))
        answer+=Min[item]
        break
  
  for i in range(len(small)):
    answer+=Min[small[i]]
  return answer

Min={}
Max={}
for i in range(2,8):
  Min[i]=''
  Max[i]=''

Min[6]='0'
Min[2]='1'
Max[2]='1'
Min[5]='2'
Min[4]='4'
Max[4]='4'
Max[5]='5'
Min[3]='7'
Max[3]='7'
Min[7]='8'
Max[7]='8'
Max[6]='9'

t=int(input())
for _ in range(t):
  n=int(input())
  # 작은 수는 일의자리수부터 성냥 많이 쓰기
  small=findMin(n)


  # 큰 수는 일의 자리수부터 성냥 아껴 쓰기
  big=deque([])
  cnt=0
  while cnt<n:
    if n-(cnt+2)==1:
      cnt+=3
      big.appendleft(Max[3])
    else:
      cnt+=2
      big.appendleft(Max[2])

  print(small,''.join(big))
