import sys
from collections import deque
input=sys.stdin.readline

def change():
  for i in range(10):
    info[i]=[[] for j in range(7)]

  info[0][0].append(0)
  info[0][4].append(1)
  info[0][3].append(2)
  info[0][3].append(3)
  info[0][4].append(4)
  info[0][3].append(5)
  info[0][2].append(6)
  info[0][3].append(7)
  info[0][1].append(8)
  info[0][2].append(9)

  info[1][4].append(0)
  info[1][0].append(1)
  info[1][5].append(2)
  info[1][3].append(3)
  info[1][2].append(4)
  info[1][5].append(5)
  info[1][6].append(6)
  info[1][1].append(7)
  info[1][5].append(8)
  info[1][4].append(9)

  info[2][3].append(0)
  info[2][5].append(1)
  info[2][0].append(2)
  info[2][2].append(3)
  info[2][5].append(4)
  info[2][4].append(5)
  info[2][3].append(6)
  info[2][4].append(7)
  info[2][2].append(8)
  info[2][3].append(9)

  info[3][3].append(0)
  info[3][3].append(1)
  info[3][2].append(2)
  info[3][0].append(3)
  info[3][3].append(4)
  info[3][2].append(5)
  info[3][3].append(6)
  info[3][2].append(7)
  info[3][2].append(8)
  info[3][1].append(9)

  info[4][4].append(0)
  info[4][2].append(1)
  info[4][5].append(2)
  info[4][3].append(3)
  info[4][0].append(4)
  info[4][3].append(5)
  info[4][4].append(6)
  info[4][3].append(7)
  info[4][3].append(8)
  info[4][2].append(9)

  info[5][3].append(0)
  info[5][5].append(1)
  info[5][4].append(2)
  info[5][2].append(3)
  info[5][3].append(4)
  info[5][0].append(5)
  info[5][1].append(6)
  info[5][4].append(7)
  info[5][2].append(8)
  info[5][1].append(9)

  info[6][2].append(0)
  info[6][6].append(1)
  info[6][3].append(2)
  info[6][3].append(3)
  info[6][4].append(4)
  info[6][1].append(5)
  info[6][0].append(6)
  info[6][5].append(7)
  info[6][1].append(8)
  info[6][2].append(9)

  info[7][3].append(0)
  info[7][1].append(1)
  info[7][4].append(2)
  info[7][2].append(3)
  info[7][3].append(4)
  info[7][4].append(5)
  info[7][5].append(6)
  info[7][0].append(7)
  info[7][4].append(8)
  info[7][3].append(9)

  info[8][1].append(0)
  info[8][5].append(1)
  info[8][2].append(2)
  info[8][2].append(3)
  info[8][3].append(4)
  info[8][2].append(5)
  info[8][1].append(6)
  info[8][4].append(7)
  info[8][0].append(8)
  info[8][1].append(9)

  info[9][2].append(0)
  info[9][4].append(1)
  info[9][3].append(2)
  info[9][1].append(3)
  info[9][2].append(4)
  info[9][1].append(5)
  info[9][2].append(6)
  info[9][3].append(7)
  info[9][1].append(8)
  info[9][0].append(9)

def find(idx,cnt,total): # 바꿀 자릿수, 바꾼 횟수, 현재 숫자
  global answer,N,P,K
  if idx==K:
    if cnt!=0 and total not in answers and total!=0:
      answers[total]=True
      answer+=1
    return

  now=int(num[idx])
  for i in range(P-cnt+1):
    if i==7:
      break
    for changeNum in info[now][i]:
      if total+changeNum*(10**(K-idx-1))<=N:
        find(idx+1,cnt+i,total+changeNum*(10**(K-idx-1)))



N,K,P,X=map(int,input().split())

# 수는 1~N이하
# K 자리수
# 최소 1개 최대 P개 반전
# 현재 X 층

info={}
change()

num=deque(list(str(X)))
for _ in range(K-len(num)):
  num.appendleft('0')

answer=0
answers={}
find(0,0,0)
print(answer)
