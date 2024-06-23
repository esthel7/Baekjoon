import sys
input=sys.stdin.readline

N=int(input())
K=int(input())
l=list(map(int,input().split()))
l.sort()

total=0
diff=[]
for i in range(N-1):
  diff.append([l[i+1]-l[i],i+1])
  total+=l[i+1]-l[i]
diff.sort()

for i in range(K-1):
  if not diff:
    print(0)
    exit(0)
  value,start=diff.pop()
  total-=value

print(total)
