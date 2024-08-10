import sys
input=sys.stdin.readline

N=int(input())
l=input().rstrip().split()

answer=['' for i in range(N+1)]
start=9
for i in range(N):
  if l[i]=='<':
    continue
  else:
    for j in range(i,-1,-1):
      if answer[j]!='':
        break
      answer[j]=str(start)
      start-=1

for i in range(N,-1,-1):
  if answer[i]=='':
    answer[i]=str(start)
    start-=1
  else:
    break

print(''.join(answer))

answer=['' for i in range(N+1)]
start=N
for i in range(N-1,-1,-1):
  if l[i]=='>':
    continue
  else:
    for j in range(i+1,N+1):
      if answer[j]!='':
        break
      answer[j]=str(start)
      start-=1

for i in range(N+1):
  if answer[i]=='':
    answer[i]=str(start)
    start-=1
  else:
    break

print(''.join(answer))
