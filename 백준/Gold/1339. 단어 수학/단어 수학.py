import sys
import heapq
input=sys.stdin.readline


N=int(input())
words=[]
info={}

for _ in range(N):
  now=list(input().rstrip())
  words.append(now)

  Now=len(now)
  for i in range(Now):
    word=now[i]
    value=10**(Now-i-1)

    if word in info:
      info[word]+=value
    else:
      info[word]=value

q=[]
for word in info.keys():
  heapq.heappush(q,[-info[word],word])

value=9
final={}
while q:
  now,word=heapq.heappop(q)
  final[word]=value
  value-=1

answer=[]
for word in words:
  now=0
  for item in word:
    now*=10
    now+=final[item]
  answer.append(now)

print(sum(answer))
