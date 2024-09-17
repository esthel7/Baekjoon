import sys
input=sys.stdin.readline

l=[]
for i in range(8):
  now=int(input())
  l.append([now,i+1])

l.sort(reverse=True)
total=0
numbers=[]
for i in range(5):
  total+=l[i][0]
  numbers.append(l[i][1])

numbers.sort()
print(total)
for answer in numbers:
  print(answer,end=' ')
print()
