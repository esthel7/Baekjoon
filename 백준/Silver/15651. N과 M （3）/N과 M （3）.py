import sys
input=sys.stdin.readline

def find():
    if len(s)==M:
        # for i in range(len(s)):
        #     print(s[i],end=' ')
        # print()
        print(' '.join(map(str,s)))
        # for문 대신 사용, join은 문자형만 가능, map(함수(자료형), 배열)를 통해 s는 변경하지 않고 문자열로 새로운 배열 만들기
        return # 중복을 체크하는 배열이 없으므로 return 필수

    for i in range(N):
        s.append(i+1) # 중복을 허용하므로 visited 배열로 중복을 관리할 필요 x -> visited를 M까지 증가시켜도 가능하나, 시간초과
        find()
        s.pop()

N,M=map(int,input().split())

s=[]
find()
