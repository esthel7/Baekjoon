import sys
input=sys.stdin.readline

def change(l,k):
  info={ 'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}
  for i in range(k):
    l[i]=info[l[i]]
  return l


k=int(input()) # 참가한 사람 수
n=int(input()) # 전체 가로줄 수
final=list(input().rstrip())
final=change(final,k)
first=[i for i in range(k)]

l=[]
for i in range(n):
  l.append(list(input().rstrip()))

blank=0
before=[-1 for i in range(k)]
for i in range(k):
  now=i
  for j in range(n):
    if l[j][0]=='?':
      blank=j
      before[now]=i
      break
    if now<k-1 and l[j][now]=='-':
      now+=1
    elif now-1>=0 and l[j][now-1]=='-':
      now-=1

after=[-1 for i in range(k)]
for i in range(k):
  now=i
  for j in range(n-1,blank,-1):
    if now<k-1 and l[j][now]=='-':
      now+=1
    elif now-1>=0 and l[j][now-1]=='-':
      now-=1
  after[now]=final[i]

answer=['*' for i in range(k-1)]
i=0
while i<k-1:
  if before[i]==after[i]:
    i+=1
    continue
  if before[i]==after[i+1] and before[i+1]==after[i]:
    answer[i]='-'
    i+=2
  else:
    answer=['x' for _ in range(k-1)]
    break

print(''.join(answer))
