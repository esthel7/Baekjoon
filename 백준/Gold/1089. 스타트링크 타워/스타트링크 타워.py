import sys
input = sys.stdin.readline
n = int(input())

# 문제에서 주어진 숫자 표현
numbs = """###...#.###.###.#.#.###.###.###.###.###
#.#...#...#...#.#.#.#...#.....#.#.#.#.#
#.#...#.###.###.###.###.###...#.###.###
#.#...#.#.....#...#...#.#.#...#.#.#...#
###...#.###.###...#.###.###...#.###.###""".split()

# 전구의 위치에 따라 만들 수 있는 숫자 후보
can_make = dict()

def make_candidates():
    for i in range(5):
        for j in range(3):
            can_make[(i,j)] = set()
            # 만들 수 있는 숫자라면 추가
            for k in range(10):
                if numbs[i][j+k*4] == "#":
                    can_make[(i,j)].add(k)

def sol():
    numb = [input() for _ in range(5)]
    res = 0.0
    for s in range(n): # 앞에서부터 5*3 판을 훑음
        can_ = set(range(10)) # 초기에는 모든 숫자를 만들 수 있다 가정
        for i in range(5):
            for j in range(s*4,s*4+3):
                if numb[i][j] == "#":
                    can_ &= can_make[(i,j%4)] # 해당 전구가 켜졌을 때 만들 수 있는 숫자와 교집합을 구함
        
        # 해당 5*3 판에서 만들 수 있는 숫자들의 평균을 구하여 더해준다.
        # 앞의 수부터 더했기 때문에 *10을 통해 자릿수를 맞춘다.
        if can_:
            res *= 10
            res += sum(can_)/len(can_)
        else:
            res = -1
            break # 한 개라도 후보자가 없다면 망가진 안내판이다.

    print(res)
    
make_candidates()
sol()