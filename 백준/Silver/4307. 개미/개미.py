import sys

 

T = int(sys.stdin.readline())

for i in range(T):

    L, N = map(int, sys.stdin.readline().split())

    ants_location = []

    for i in range(N):

        ants_location.append(int(sys.stdin.readline()))

    ants_location.sort()

    min_time = 0

    max_time = 0

    for ant in ants_location:

        min_time = max(min_time, min(ant, L-ant))

        max_time = max(max_time, ant, L-ant)

    print(min_time, max_time)