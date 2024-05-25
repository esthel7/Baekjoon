import sys
input=sys.stdin.readline

N,M=map(int,input().split())
group={}
person={}
for i in range(N):
  gname=input().rstrip()
  group[gname]=[]
  num=int(input())
  for j in range(num):
    pname=input().rstrip()
    group[gname].append(pname)
    person[pname]=gname
  group[gname].sort()

for i in range(M):
  name=input().rstrip()
  num=int(input())
  if num==0:
    for pname in group[name]:
      print(pname)
  else:
    print(person[name])
