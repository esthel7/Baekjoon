import sys
input=sys.stdin.readline

def find():
    if P in S: # P가 S에 들어있는지 확인
        print(1)
    else:
        print(0)

S=input().rstrip() # 엔터키 제거
P=input().rstrip()

# print(S)
# print(P)

if len(P)<=len(S):
    find()
else:
    print(0)
