import sys
import heapq
from collections import deque
input=sys.stdin.readline

N=int(input())
first=[]
l=[]
heapq.heapify(l)
for i in range(N):
  now=input().rstrip()
  first.append(now)
  heapq.heappush(l,[now,i])

Max=0
MaxList=[]
info={}

word=''
Len=0
words,idx=heapq.heappop(l)
for str in words:
  word+=str
  Len+=1
  info[Len]={word:[1,deque([idx])]} # cnt, idx
# print(words,info)

while l:
  word=''
  Len=0
  words,idx=heapq.heappop(l)
  for str in words:
    word+=str
    Len+=1
    if Len>=Max:
      if Len in info and word in info[Len]:
        if info[Len][word][0]==2:
          if info[Len][word][1][0]>idx:
            info[Len][word][1].pop()
            info[Len][word][1].appendleft(idx)
          elif info[Len][word][1][1]>idx:
            info[Len][word][1].pop()
            info[Len][word][1].append(idx)
          if MaxList and MaxList[0]>info[Len][word][1][0]:
            MaxList=list(info[Len][word][1])
        else:
          info[Len][word][0]=2
          if info[Len][word][1][0]<idx:
            info[Len][word][1].append(idx)
          else:
            info[Len][word][1].appendleft(idx)
          if Len>Max:
            Max=Len
            MaxList=list(info[Len][word][1])
          elif not MaxList or (MaxList and MaxList[0]>info[Len][word][1][0]):
            MaxList=list(info[Len][word][1])
      else:
        info[Len]={word:[1,deque([idx])]}
  # print(words,info,Max,MaxList)


if Max==0:
  print(first[0])
  print(first[1])
else:
  print(first[MaxList[0]])
  print(first[MaxList[1]])

# 8
# ab
# abc
# xywxa
# noone
# abcd
# abcde
# noon
# xywx
