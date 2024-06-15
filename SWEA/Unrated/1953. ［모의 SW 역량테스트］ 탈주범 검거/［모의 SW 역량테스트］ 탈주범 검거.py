# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제 
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''




'''
아래의 구문은 input.txt 를 read only 형식으로 연 후,
앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.
따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
아래 구문을 사용하기 위해서는 import sys가 필요합니다.
단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''

'''
5
5 6 2 1 3
0 0 5 3 6 0
0 0 2 0 2 0
3 3 1 3 7 0
0 0 0 0 0 0
0 0 0 0 0 0
5 6 2 1 3
0 0 5 3 6 0
0 0 2 0 2 0
3 3 1 3 7 0
0 0 0 0 0 0
0 0 0 0 0 0
5 6 2 1 3
0 0 5 3 6 0
0 0 2 0 2 0
3 3 1 3 7 0
0 0 0 0 0 0
0 0 0 0 0 0
5 6 2 1 3
0 0 5 3 6 0
0 0 2 0 2 0
3 3 1 3 7 0
0 0 0 0 0 0
0 0 0 0 0 0
5 6 2 1 3
0 0 5 3 6 0
0 0 2 0 2 0
3 3 1 3 7 0
0 0 0 0 0 0
0 0 0 0 0 0
'''
#import sys
#sys.stdin = open("input.txt", "r")

from collections import deque

TOP=[1,2,5,6]
BOTTOM=[1,2,4,7]
LEFT=[1,3,4,5]
RIGHT=[1,3,6,7]

def find(R,C):
    global answer
    visited=[[False for i in range(M)]for j in range(N)]
    
    def top(x,y,time):
        global answer
        if x-1>=0 and not visited[x-1][y]:
            if l[x-1][y] in TOP:
                visited[x-1][y]=True
                answer+=1
                if time+1<L:
                    q.append([x-1,y,time+1])

    def bottom(x,y,time):
        global answer
        if x+1<N and not visited[x+1][y]:
            if l[x+1][y] in BOTTOM:
                visited[x+1][y]=True
                answer+=1
                if time+1<L:
                    q.append([x+1,y,time+1])
                    
    def left(x,y,time):
        global answer
        if y-1>=0 and not visited[x][y-1]:
            if l[x][y-1] in LEFT:
                visited[x][y-1]=True
                answer+=1
                if time+1<L:
                    q.append([x,y-1,time+1])

    def right(x,y,time):
        global answer
        if y+1<M and not visited[x][y+1]:
            if l[x][y+1] in RIGHT:
                visited[x][y+1]=True
                answer+=1
                if time+1<L:
                    q.append([x,y+1,time+1])
    
    q=deque([[R,C,1]])
    answer+=1
    visited[R][C]=True
    if L==1:
    	return
    while q:
        x,y,time=q.popleft()
        if l[x][y]==1:
            top(x,y,time)
            bottom(x,y,time)
            left(x,y,time)
            right(x,y,time)
        elif l[x][y]==2:
            top(x,y,time)
            bottom(x,y,time)
        elif l[x][y]==3:
            left(x,y,time)
            right(x,y,time)
        elif l[x][y]==4:
            top(x,y,time)
            right(x,y,time)
        elif l[x][y]==5:
            bottom(x,y,time)
            right(x,y,time)
        elif l[x][y]==6:
            bottom(x,y,time)
            left(x,y,time)
        elif l[x][y]==7:
            top(x,y,time)
            left(x,y,time)
            
        

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N,M,R,C,L=map(int,input().split())
    answer=0
    l=[]
    for i in range(N):
        l.append(list(map(int,input().split())))
    find(R,C)
    print('#%d %d'%(test_case,answer))