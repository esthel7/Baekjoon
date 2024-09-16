import sys
input=sys.stdin.readline

N=int(input())
l=[]
for i in range(N):
  name,kor,eng,math=input().rstrip().split()
  kor=int(kor)
  eng=int(eng)
  math=int(math)
  l.append([kor,eng,math,name])
l.sort(key=lambda x:[-x[0],x[1],-x[2],x[3]])

for i in range(N):
  print(l[i][3])
