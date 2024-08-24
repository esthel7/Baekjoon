import sys
input=sys.stdin.readline

change={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8}
changeChar={1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H'}

king,rock,N=input().rstrip().split()
king=list(king)
king[0]=change[king[0]]
king[1]=int(king[1])
rock=list(rock)
rock[0]=change[rock[0]]
rock[1]=int(rock[1])
N=int(N)

for i in range(N):
  move=list(input().rstrip())
  if len(move)==1:
    if move[0]=='R' and king[0]<8:
      if rock[1]==king[1] and rock[0]==king[0]+1:
        if rock[0]<8:
          king[0]+=1
          rock[0]+=1
      else:
        king[0]+=1
    elif move[0]=='L' and king[0]>1:
      if rock[1]==king[1] and rock[0]==king[0]-1:
        if rock[0]>1:
          king[0]-=1
          rock[0]-=1
      else:
        king[0]-=1
    elif move[0]=='B' and king[1]>1:
      if rock[0]==king[0] and rock[1]==king[1]-1:
        if rock[1]>1:
          king[1]-=1
          rock[1]-=1
      else:
        king[1]-=1
    elif move[0]=='T' and king[1]<8:
      if rock[0]==king[0] and rock[1]==king[1]+1:
        if rock[1]<8:
          king[1]+=1
          rock[1]+=1
      else:
        king[1]+=1
  else:
    if move[0]=='R' and king[0]<8 and move[1]=='T' and king[1]<8:
      if rock[0]==king[0]+1 and rock[1]==king[1]+1:
        if rock[0]<8 and rock[1]<8:
          king[0]+=1
          king[1]+=1
          rock[0]+=1
          rock[1]+=1
      else:
        king[0]+=1
        king[1]+=1
    elif move[0]=='R' and king[0]<8 and move[1]=='B' and king[1]>1:
      if rock[0]==king[0]+1 and rock[1]==king[1]-1:
        if rock[0]<8 and rock[1]>1:
          king[0]+=1
          king[1]-=1
          rock[0]+=1
          rock[1]-=1
      else:
        king[0]+=1
        king[1]-=1
    elif move[0]=='L' and king[0]>1 and move[1]=='T' and king[1]<8:
      if rock[0]==king[0]-1 and rock[1]==king[1]+1:
        if rock[0]>1 and rock[1]<8:
          king[0]-=1
          king[1]+=1
          rock[0]-=1
          rock[1]+=1
      else:
        king[0]-=1
        king[1]+=1
    elif move[0]=='L' and king[0]>1 and move[1]=='B' and king[1]>1:
      if rock[0]==king[0]-1 and rock[1]==king[1]-1:
        if rock[0]>1 and rock[1]>1:
          king[0]-=1
          king[1]-=1
          rock[0]-=1
          rock[1]-=1
      else:
        king[0]-=1
        king[1]-=1

print(changeChar[king[0]],end='')
print(king[1])
print(changeChar[rock[0]],end='')
print(rock[1])
