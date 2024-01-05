import sys
input=sys.stdin.readline

k=int(input())
l=[]
n=0
for i in range(k):
  a=int(input())
  if a==0:
    d=l.pop()
    n-=d
  else:
    l.append(a)
    n+=a
print(n)
