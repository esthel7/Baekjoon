import sys
from collections import deque
input=sys.stdin.readline

T=int(input())
for _ in range(T):
  N=int(input())
  l=[]
  for i in range(N):
    l.append(list(map(int,input().split())))
  l.sort()
  # print(l)

  answer=1
  value=l[0][1]
  for i in range(1,N):
    if value>=l[i][1]:
      answer+=1
      value=l[i][1]
  print(answer)

# 1
# 7
# 3 6
# 7 3
# 1 4
# 5 7
# 2 5
# 6 1
# 6 2
  
# 1
# 6
# 1 6
# 5 1
# 3 4
# 4 3
# 2 2
# 6 5
