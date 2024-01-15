import sys
# from collections import deque
input=sys.stdin.readline

def find(K,start,num):
  if len(num)==6:
    for answer in num:
      print(answer,end=' ')
    print()
    return
  if start==K:
    return

  for i in range(start,K):
    num.append(l[i])
    find(K,i+1,num)
    num.pop()

while True:
  l=list(map(int,input().split()))
  K=l[0]
  if K==0:
    break
  l.pop(0)
  l.sort()
  find(K,0,[])
  print()
