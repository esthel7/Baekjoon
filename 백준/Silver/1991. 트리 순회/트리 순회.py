import sys
input=sys.stdin.readline

def first(node):
  print(node,end='')
  if node in left:
    first(left[node])
  if node in right:
    first(right[node])

def mid(node):
  if node in left:
    mid(left[node])
  print(node,end='')
  if node in right:
    mid(right[node])

def last(node):
  if node in left:
    last(left[node])
  if node in right:
    last(right[node])
  print(node,end='')


N=int(input())
left={}
right={}
for i in range(N):
  a,b,c=input().rstrip().split()
  if b!='.':
    left[a]=b
  if c!='.':
    right[a]=c

first('A')
print()
mid('A')
print()
last('A')
print()

